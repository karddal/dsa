from solutions.arrays_hashing.group_anagrams import Solution


def test_basic():
    assert sorted(Solution().groupAnagrams(["abc", "bac", "cba", "ddd"])) == sorted(
        [sorted(["abc", "bac", "cba"]), sorted(["ddd"])]
    )


def test_all():
    assert sorted(Solution().groupAnagrams(["ab", "ba"])) == sorted(
        [sorted(["ab", "ba"])]
    )
