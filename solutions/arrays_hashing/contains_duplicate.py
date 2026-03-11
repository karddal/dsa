# 217 Contains Duplicate

# Approach - use a lookup set
# A set lets us check whether an element is in it in O(1)
# Time: O(n), Space: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
