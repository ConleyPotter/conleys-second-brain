#!/usr/bin/env python3
"""
Vault validation checks for CI.

Two checks:
1. Frontmatter validity — every wiki page (except index.md and log.md)
   must have YAML frontmatter with required fields and valid enum values.
2. log.md append-only — changes to log.md must only add lines at the end,
   never modify or remove existing lines.

Note: VALID_DOMAINS and VALID_TYPES must stay in sync with the enums defined
in CLAUDE.md.  When a new domain or type is added to doctrine, update here too.
"""

import glob
import os
import subprocess
import sys

import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WIKI_DIR = os.path.join("Conley's 2nd Brain", "wiki")

SPECIAL_FILES = {"index.md", "log.md"}

REQUIRED_FIELDS = {"type", "domain", "created", "updated"}

VALID_DOMAINS = {"ace", "ba", "personal", "research", "general", "drone-enterprises"}

VALID_TYPES = {
    "strategy",
    "operations",
    "tool-analysis",
    "marketing",
    "identity",
    "project",
    "asset",
    "synthesis",
    "work-log",
}

# ---------------------------------------------------------------------------
# Frontmatter check
# ---------------------------------------------------------------------------


def extract_frontmatter(filepath: str) -> tuple[dict | None, str | None]:
    """Return (frontmatter_dict, error_string). One of them is always None."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as exc:
        return None, f"Could not read file: {exc}"

    if not content.startswith("---"):
        return None, "Missing frontmatter (file does not start with '---')"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Malformed frontmatter (no closing '---')"

    raw_yaml = parts[1]
    try:
        fm = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        return None, f"Invalid YAML in frontmatter: {exc}"

    if not isinstance(fm, dict):
        return None, "Frontmatter is not a YAML mapping"

    return fm, None


def check_frontmatter() -> list[str]:
    """Validate frontmatter on all wiki pages (except special files)."""
    errors: list[str] = []

    if not os.path.isdir(WIKI_DIR):
        # If the wiki dir doesn't exist in this diff, nothing to check.
        return errors

    pattern = os.path.join(WIKI_DIR, "*.md")
    for filepath in sorted(glob.glob(pattern)):
        basename = os.path.basename(filepath)
        if basename in SPECIAL_FILES:
            continue

        fm, err = extract_frontmatter(filepath)
        if err:
            errors.append(f"{filepath}: {err}")
            continue

        # Required fields
        missing = REQUIRED_FIELDS - set(fm.keys())
        if missing:
            errors.append(
                f"{filepath}: Missing required frontmatter fields: {', '.join(sorted(missing))}"
            )

        # Domain enum
        domain = fm.get("domain")
        if domain is not None and str(domain) not in VALID_DOMAINS:
            errors.append(
                f"{filepath}: Invalid domain '{domain}'. "
                f"Must be one of: {', '.join(sorted(VALID_DOMAINS))}"
            )

        # Type enum
        page_type = fm.get("type")
        if page_type is not None and str(page_type) not in VALID_TYPES:
            errors.append(
                f"{filepath}: Invalid type '{page_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_TYPES))}"
            )

    return errors


# ---------------------------------------------------------------------------
# log.md append-only check
# ---------------------------------------------------------------------------


def _get_diff_base() -> str:
    """Return the appropriate git ref to diff against.

    For pull requests (GITHUB_BASE_REF is set), use the merge-base with the
    target branch so the check covers all commits in the PR — not just the
    latest one.  For pushes, fall back to HEAD~1.
    """
    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        try:
            result = subprocess.run(
                ["git", "merge-base", f"origin/{base_ref}", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            pass
    return "HEAD~1"


def check_log_append_only() -> list[str]:
    """Ensure log.md changes only append lines at the end."""
    errors: list[str] = []

    log_path = os.path.join(WIKI_DIR, "log.md")

    # Determine the correct diff base (merge-base for PRs, HEAD~1 for pushes).
    diff_base = _get_diff_base()

    # Only check if log.md was modified in this diff range.
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", diff_base, "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        changed_files = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        # If there's no valid base (initial commit), skip this check.
        return errors

    if log_path not in changed_files:
        return errors

    # Get the diff for log.md specifically.
    try:
        result = subprocess.run(
            ["git", "diff", diff_base, "HEAD", "--", log_path],
            capture_output=True,
            text=True,
            check=True,
        )
        diff_output = result.stdout
    except subprocess.CalledProcessError:
        return errors

    if not diff_output:
        return errors

    # Parse the unified diff for two violations:
    #
    # 1. Removed lines — any line starting with '-' (but not '---') that
    #    has non-whitespace content indicates a deletion or modification.
    #
    # 2. Non-tail insertions — if added lines ('+') are followed by
    #    context lines (' ') within the same hunk, the additions are in
    #    the middle of the file rather than appended at the end.

    saw_addition_in_hunk = False

    for line in diff_output.split("\n"):
        # Hunk header resets per-hunk state.
        if line.startswith("@@"):
            saw_addition_in_hunk = False
            continue

        # Check 1: removed lines.
        if line.startswith("-") and not line.startswith("---"):
            removed_content = line[1:].strip()
            # Ignore empty-line removals (whitespace normalization).
            if removed_content:
                suffix = "..." if len(removed_content) > 80 else ""
                errors.append(
                    f"{log_path}: Non-append edit detected. "
                    f"Removed line: '{removed_content[:80]}{suffix}'"
                )
                break

        # Check 2: non-tail insertions.
        if line.startswith("+") and not line.startswith("+++"):
            saw_addition_in_hunk = True
        elif line.startswith(" ") and saw_addition_in_hunk:
            # A context line (unchanged) after an addition means content
            # exists below the insertion point — this is a mid-file insert.
            errors.append(
                f"{log_path}: Non-tail insertion detected. "
                f"Lines were added before existing content, not appended "
                f"at the end."
            )
            break

    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    errors: list[str] = []

    print("=== Vault Checks ===\n")

    print("1. Checking wiki frontmatter...")
    fm_errors = check_frontmatter()
    errors.extend(fm_errors)
    if fm_errors:
        for e in fm_errors:
            print(f"   FAIL: {e}")
    else:
        print("   OK")

    print("\n2. Checking log.md append-only...")
    log_errors = check_log_append_only()
    errors.extend(log_errors)
    if log_errors:
        for e in log_errors:
            print(f"   FAIL: {e}")
    else:
        print("   OK")

    print()

    if errors:
        print(f"FAILED: {len(errors)} error(s) found.")
        return 1
    else:
        print("PASSED: All vault checks passed.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
