"""
lsh.py

Algorithms based on 'Mining of Massive Datasets'
"""
import lshhdc.signature
import lshhdc.unionfind


class LSH:
    """Locality sensitive hashing.  Uses a banding approach to hash
    similar signatures to the same buckets."""

    def __init__(self, length, threshold):
        self.length = length
        self.threshold = threshold
        self.bandwidth = self.get_bandwidth(length, threshold)

    def hash(self, sig):
        """Generate hashvals for this signature"""
        for band in zip(*(iter(sig),) * self.bandwidth):
            yield hash("salt" + str(band) + "tlas")

    def get_bandwidth(self, n, t):
        """Approximates the bandwidth (number of rows in each band)
        needed to get threshold.  
        
        Threshold t = (1/b) ** (1/r) where
        b = #bands
        r = #rows per band
        n = b * r = #elements in signature
        """

        best = n, 1
        minerr = float("inf")
        for r in range(1, n + 1):
            try:
                b = 1. / (t ** r)
            except:             # Divide by zero, your signature is huge
                return best
            err = abs(n - b * r)
            if err < minerr:
                best = r
                minerr = err
        return best

    def get_threshold(self):
        r = self.bandwidth
        b = self.length / r
        return (1. / b) ** (1. / r)