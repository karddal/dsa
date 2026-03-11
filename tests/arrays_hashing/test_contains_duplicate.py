from solutions.arrays_hashing.contains_duplicate import Solution


def test_basic():
    assert not Solution().containsDuplicate([1, 2, 3, 4])


def test_duplicate():
    assert Solution().containsDuplicate([1, 2, 3, 3])


def test_single():
    assert not Solution().containsDuplicate([1])
