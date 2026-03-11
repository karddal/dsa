from solutions.arrays_hashing.two_sum import Solution


def test_basic():
    assert sorted(Solution().twoSum([1, 2, 3, 4], 7)) == [2, 3]


def test_middle():
    assert sorted(Solution().twoSum([0, 5, 6, 2], 11)) == [1, 2]


def test_start_end():
    assert sorted(Solution().twoSum([1, 0, 0, 1], 2)) == [0, 3]
