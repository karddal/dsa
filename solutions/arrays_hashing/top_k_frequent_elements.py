# 347 Top K Frequent Elements
#
# We need to return the top k most frequent elements of the array.
# Approach: Keep running tally of all frequencies
# Then assign letters to frequency buckets
# Then build the output based on k from this frequency bucket array.
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequencies.items():
            buckets[freq].append(num)

        output = []
        for i in range(len(nums), -1, -1):
            for number in buckets[i]:
                output.append(number)
                if len(output) == k:
                    return output

        return []
