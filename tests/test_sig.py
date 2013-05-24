import math

import lshhdc.utils
import lshhdc.signature


def test_signature_length():
    """Signatures should have correct dimension"""
    dim = 100
    mh = lshhdc.signature.MinHashSignature(dim)
    assert dim == len(mh.sign(lshhdc.utils.randset()))


def test_consistent_signature():
    """Signatures should be consistent"""
    mh = lshhdc.signature.MinHashSignature(100)
    s = lshhdc.utils.randset()
    assert mh.sign(s) == mh.sign(s)


def test_signature_similarity():
    """The probability that two sets' signatures match at some index
    are equal is equal to the Jaccard similarity between the two"""
    dim = 100
    n_tests = 100
    expected_error = 1 / math.sqrt(dim) # Expected error is O(1/sqrt(dim))
    mh = lshhdc.signature.MinHashSignature(dim)
    err = 0.0

    for test in range(n_tests):
        # Create random sets and their signatures
        sets = (lshhdc.utils.randset(), lshhdc.utils.randset())
        sigs = map(mh.sign, sets)

        # Calculate true jaccard similarity, and sim of signatures
        jsim = lshhdc.utils.jaccard_sim(*sets)
        ssim = lshhdc.utils.sigsim(*sigs, dim=dim)

        # Accumulate error
        err += abs(jsim - ssim)

    # Over n_tests large, we should be within upper bound of expected error.
    avg_err = err / n_tests
    assert expected_error >= avg_err, "Accuracy test failed. (avg error: %f)" % avg_err
