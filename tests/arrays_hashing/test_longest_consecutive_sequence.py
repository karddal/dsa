from solutions.arrays_hashing.longest_consecutive_sequence import Solution


def test_basic():
    assert Solution().longestConsecutive([50, 3, 100, 2, 1]) == 3


def test_negatives():
    assert Solution().longestConsecutive([500, -100, -99, -98, 1]) == 3
