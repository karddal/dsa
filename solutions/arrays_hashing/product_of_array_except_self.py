# 238 Product of Array Except Self

# Approach - keep a prefix and a suffix sum
# In the output, we can multiply the prefix and suffix sum for each position to get the
# product of every element except that element.
# We are allowed negative numbers in the input so we need to be careful of that.

# Time: O(n)
# Space: O(1) if we exclude the output array


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
