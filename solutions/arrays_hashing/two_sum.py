# 1 Two Sum

# Problem - given an array of ints, and a target number, return the indices of two numbers in array that will sum to the target
# Guaranteed to have exactly 1 solution.
#
# Approach - Using a hashmap, we can keep track of the indices of numbers that we have encountered
# Iterating over the array, we can check whether the number we would add to the current number to form the target
# has been encountered already. If it has, we can output the indices. If not, update the hashmap with the current number
# and its index.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        locs = {}

        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in locs:
                return [i, locs[goal]]

            locs[nums[i]] = i

        assert False  # LeetCode problem guarantees a solution, I add this to satisfy the typechecker.
