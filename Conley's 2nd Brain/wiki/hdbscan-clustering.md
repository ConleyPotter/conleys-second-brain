---
type: synthesis
domain: general
tags: [machine-learning, clustering, hdbscan, unsupervised-learning, python, scikit-learn, density-based]
created: 2026-06-07
updated: 2026-06-07
sources: [google-ai-mode-hdbscan-clustering-2026-06-07.md]
---

# HDBSCAN Clustering

**Related:** [[domain-general]]

---

## What HDBSCAN is

HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is an unsupervised machine learning algorithm that identifies dense regions in data to form clusters. It extends DBSCAN by handling variable-density clusters and automatically determining the optimal number of clusters — no need to specify `k` upfront. Points in sparse regions are classified as noise (label `-1`).

The key differentiator from DBSCAN: instead of a single global density threshold (ε), HDBSCAN builds a full cluster hierarchy and extracts the most stable groupings across density scales.

---

## How it works

1. **Mutual reachability distance** — transforms pairwise distances to penalize points in low-density areas, creating a density-aware distance metric.
2. **Minimum spanning tree** — connects all data points using the mutual reachability distances.
3. **Cluster hierarchy** — breaks the tree apart into a dendrogram of potential clusters at every density level.
4. **Stable cluster extraction** — condenses the hierarchy, keeping only clusters that persist over a wide range of density scales. Transient groupings are discarded.

---

## Why it matters

- **Variable density** — finds clusters of drastically different densities within the same dataset. Standard DBSCAN cannot do this.
- **Noise tolerance** — points that don't belong to any dense, cohesive group are automatically labeled as noise. No forced assignment.
- **Minimal tuning** — the main parameter is `min_cluster_size`. Increasing it merges smaller clusters into larger ones or into noise. Far less tuning than k-means or DBSCAN.
- **Soft clustering** — provides membership probabilities rather than just hard labels, giving a confidence measure for each assignment.

---

## Implementation

HDBSCAN follows the scikit-learn API. The `hdbscan` package from scikit-learn-contrib is the standard implementation:

```bash
pip install hdbscan
```

```python
import hdbscan
from sklearn.datasets import make_blobs

data, _ = make_blobs(n_samples=500, centers=5, cluster_std=0.5, random_state=42)
clusterer = hdbscan.HDBSCAN(min_cluster_size=15, min_samples=5)
cluster_labels = clusterer.fit_predict(data)
```

Key parameters:
- `min_cluster_size` — minimum number of points for a grouping to count as a cluster (start here for tuning)
- `min_samples` — controls how conservative the clustering is; higher values = more points classified as noise
- Tree-cutting strategies: `eom` (excess of mass, default) vs. `leaf` (flat cut at the leaves)

---

## Common use cases

- **Topic modeling** — BERTopic uses HDBSCAN as its default clustering backend on sentence embeddings
- **Geospatial analytics** — identifying population centers, delivery zones, movement patterns
- **Genomics** — clustering gene expression data without pre-specifying the number of groupings
- **UMAP + HDBSCAN pipeline** — a common pattern: reduce dimensionality with UMAP, then cluster the embedded points with HDBSCAN

---

## Resources

- [hdbscan Read the Docs](https://hdbscan.readthedocs.io/) — full API reference, caching, tree-cutting strategies
- [How HDBSCAN Works](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html) — step-by-step algorithm walkthrough
- [Scikit-learn HDBSCAN Module](https://scikit-learn.org/stable/modules/clustering.html#hdbscan) — usage in standard ML pipelines