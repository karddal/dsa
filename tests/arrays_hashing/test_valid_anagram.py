from solutions.arrays_hashing.valid_anagram import Solution


def test_basic():
    assert Solution().isAnagram("abb", "bab")


def test_not_anagram():
    assert not Solution().isAnagram("abc", "def")


def test_single_not():
    assert not Solution().isAnagram("a", "b")


def test_single():
    assert Solution().isAnagram("a", "a")
