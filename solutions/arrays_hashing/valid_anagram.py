# 242 Valid Anagram

# Approach - two strings are anagrams if they have the same number
# of each character.
# We can assume that we only have lowercase English letters, so we
# can store the number of each character present as a list so O(1) space.

# Time: O(n)
# Space: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[ord(s[i]) - ord("a")] += 1
            countT[ord(t[i]) - ord("a")] += 1

        return countS == countT
