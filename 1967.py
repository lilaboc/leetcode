# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(i in word for i in patterns )

print(Solution().numOfStrings(["a","abc","bc","d"], "abc"))
