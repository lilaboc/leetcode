# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def __init__(self):
        self.d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        return list(self.combine(digits))

    def combine(self, digits):
        if len(digits) == 1:
            return self.d[digits]
        if len(digits) == 0:
            return []
        return ((i + o  for o in self.combine(digits[1:]) for i in self.d[digits[0]])) 

print(Solution().letterCombinations("234"))