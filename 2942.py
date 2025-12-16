# https://leetcode.com/problems/find-words-containing-character/description/
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result



