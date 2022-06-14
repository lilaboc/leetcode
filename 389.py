# https://leetcode.com/problems/find-the-difference/
from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = Counter(t)
        s = Counter(s)
        for i in t.keys():
            if i not in s or t[i] > s[i]:
                return i



print(Solution().findTheDifference("", "y"))
print(Solution().findTheDifference("abcd", "abcde"))
