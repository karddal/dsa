# 138 Longest Consecutive Sequence

# Approach:
# We need to be able to make presence checks in O(1) time so create a set
# For each element, we can check whether the previous element is in the set
# If it is not, we have found a potential new sequence and try to build one

# Time: O(n)
# Space: O(n)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        avail = set(nums)

        longest = 0

        for num in avail:
            if num - 1 not in avail:
                # try and build a sequence
                length = 0
                while num + length in avail:
                    length += 1

                longest = max(longest, length)

        return longest
