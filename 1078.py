# https://leetcode.com/problems/occurrences-after-bigram/
from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        terms = text.split()
        for i in range(len(terms) - 2):
            if terms[i] == first and terms[i + 1] == second:
                result.append(terms[i + 2])
        return result
            

print(Solution().findOcurrences(text = "we will we will rock you", first = "we", second = "will"))