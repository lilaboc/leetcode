# https://leetcode.com/problems/count-prefixes-of-a-given-string/
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(1 for word in words if s.startswith(word))

