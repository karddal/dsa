# 49 Group Anagrams

# Approach - Anagrams are uniquely identified by their character counts
# Using a hashmap of lists, key = Character count array, value = list
# Group them together
# Output just the lists.

# Space: O(n)
# Time: O(n)

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26  # we can assume only lowercase

            for c in s:
                counts[ord(c) - ord("a")] += 1

            groups[tuple(counts)].append(s)

        return list(
            groups.values()
        )  # .values() is some weird DictValues iterator, need to convert it to a list.
