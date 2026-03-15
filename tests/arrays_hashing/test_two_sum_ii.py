from solutions.arrays_hashing.two_sum_ii import Solution


def test_basic():
    assert Solution().twoSum([2, 4, 5, 9], 9) == [2, 3]


def test_negatives():
    assert Solution().twoSum([-50, -10, 2, 3], -8) == [2, 3]
