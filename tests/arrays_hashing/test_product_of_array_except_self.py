from solutions.arrays_hashing.product_of_array_except_self import Solution


def test_basic():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_with_negatives():
    assert Solution().productExceptSelf([-1, -4, 2, 1]) == [-8, -2, 4, 8]
