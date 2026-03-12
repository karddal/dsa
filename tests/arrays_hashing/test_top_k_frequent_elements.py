from solutions.arrays_hashing.top_k_frequent_elements import Solution


def test_basic():
    assert Solution().topKFrequent([1, 2, 1, 1], 1) == [1]


def test_more():
    assert sorted(Solution().topKFrequent([1, 2, 2, 1, 3], 2)) == [1, 2]


def test_edge():
    assert Solution().topKFrequent([1], 1) == [1]
