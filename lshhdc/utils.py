"""
utils.py

Testing utilities
"""
import random
import operator


def randset():
    """Return a random set.  These values of n and k have wide-ranging
    similarities between pairs.
    """
    n = random.choice(range(5, 20))
    k = 10
    return tuple(set(random.choice(range(k)) for _ in range(n)))


def sigsim(X, Y, dim):
    """Return the similarity of the two signatures"""
    return sum(map(operator.eq, X, Y)) / float(dim)


def shingle(s, k):
    """Generate k-length shingles of string s"""
    k = min(len(s), k)
    for i in range(len(s) - k + 1):
        yield s[i:i + k]


def hshingle(s, k):
    """Generate k-length shingles then hash"""
    for s in shingle(s, k):
        yield hash(s)


def jaccard_sim(X, Y):
    """Jaccard similarity between two sets"""
    x = set(X)
    y = set(Y)
    return float(len(x & y)) / len(x | y)


def jaccard_dist(X, Y):
    """Jaccard distance between two sets"""
    return 1 - jaccard_sim(X, Y)
