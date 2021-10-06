# https://leetcode.com/problems/count-the-number-of-consistent-strings/
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(word) <= allowed for word in words)


print(Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
