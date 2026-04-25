# Skill: Process Inbox

## Trigger phrases
"process my inbox" / "run morning capture" / "clear the inbox"

## Process

1. Read every note in `00-INBOX/`
2. For each note:
   a. Determine which `01-CAPTURES/` subfolder it belongs in:
      - `observations/` — things noticed, raw and unpolished
      - `reactions/` — honest gut response to something read or heard
      - `patterns/` — same principle appearing in two different domains
      - `questions/` — things genuinely not known
      - `numbers/` — real data points with specific numbers attached
   b. Sharpen the raw note into one specific punchy sentence —
      specific enough that a stranger understands exactly what was observed
      without additional context. If it still needs explanation, rewrite it.
   c. Add exactly three tags — no more, no fewer
   d. Move the sharpened note to the correct subfolder
3. After processing all notes, report:
   - Total notes processed and where each went
   - Any patterns noticed across today's captures
   - One connection worth exploring from today's batch

## Quality bar

A sharpened note should be specific enough that a stranger understands exactly what was observed without any additional context. If it still needs explanation, it is not sharp enough. Rewrite it.

## Example

Raw inbox note: "the pipeline was slow"
Sharpened: "Apollo enrichment returned partial results on 40% of rows when run between 11pm–1am ET — rate limits or server-side degradation at night."
Tags: `#ace` `#apollo` `#pipeline`
Folder: `observations/`
