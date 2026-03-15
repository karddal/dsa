# 125 Valid Palindrome

# Approach - we need to check whether string is the same front-to-back
# and back-to-front. We can use two pointers for this.
# We remember to ignore non-alphanumeric characters.

# Time: O(n)
# Space: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Standard two pointer recipe
        left = 0
        right = len(s) - 1

        while (
            left < right
        ):  # don't go up to right as we don't care about the middle element
            # skip over any non alphanumeric characters
            while not s[left].isalnum() and left < right:
                left += 1

            while not s[right].isalnum() and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
