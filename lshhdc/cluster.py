import lshhdc.unionfind
import lshhdc.signature
import lshhdc.lsh


class Cluster:
    """Clusters sets with Jaccard similarity above threshold with high
    probability.

    Algorithm based on Rajaraman, "Mining of Massive Datasets":
    1. Generate set signature
    2. Use LSH to map similar signatures to same buckets
    3. Use UnionFind to merge buckets containing same values
    """

    def __init__(self, width=10, threshold=0.5):
        self.width = width
        self.unionfind = lshhdc.unionfind.UnionFind()
        self.signer = lshhdc.signature.MinHashSignature(width)
        self.hasher = lshhdc.lsh.LSH(width, threshold)
        self.hashmap = {}

    def add_set(self, s, label=None):
        # A label for this set
        if not label:
            label = s

        # Add to unionfind structure
        self.unionfind[label]

        # Get signature
        sig = self.signer.sign(s)

        # Union labels with same LSH keys
        for hshval in self.hasher.hash(sig):
            self.hashmap.setdefault(hshval, []).append(label)
            self.unionfind.union(label, self.hashmap[hshval][0])

    def get_sets(self):
        return self.unionfind.sets()