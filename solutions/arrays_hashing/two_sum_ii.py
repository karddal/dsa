# 167 Two Sum II - Input Array is Sorted

# Approach: the input array is sorted in non-decreasing order.
# This means that we can use two pointers to narrow down the positions


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [
                    left + 1,
                    right + 1,
                ]  # solution requests indices incremented by 1

            if current < target:
                left += 1

            else:
                right -= 1

        assert (
            False
        )  # A solution is guaranteed by the spec, this is to satisfy the type-checker.
