class Signature:
    """Signature Base class."""

    def __init__(self, dim):
        self.dim = dim
        self.hashes = self.hash_functions()

    def hash_functions(self):
        """Returns dim different hash functions"""
        pass

    def sign(self, object):
        """Return the signature for object s"""
        pass


class MinHashSignature(Signature):
    """Creates signatures for sets/tuples using minhash."""

    def hash_functions(self):
        """Return dim different hash functions"""

        def hash_factory(n):
            return lambda x: hash("salt" + str(n) + str(x) + "salt")

        return [hash_factory(_) for _ in range(self.dim)]

    def sign(self, s):
        """Returns minhash signature for set s"""
        sig = [float("inf")] * self.dim
        for hash_ix, hash_fn in enumerate(self.hashes):
            sig[hash_ix] = min(hash_fn(value) for value in s)
        return sig
