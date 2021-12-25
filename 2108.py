# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        if l % 2 == 0:
            return s[: int(l/2)] == s[int(l/2):][::-1]
        else:
            return s[: int(l/2)] == s[int(l/2) + 1:][::-1]

    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if self.isPalindrome(i):
                return i
        return ""


print(Solution().firstPalindrome(["abc","car","ada","racecar","cool"]))