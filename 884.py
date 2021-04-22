# https://leetcode.com/problems/uncommon-words-from-two-sentences/
from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter()
        for i in A.split():
            c[i] += 1
        for i in B.split(): 
            c[i] += 1
        return [k for k, v in c.items() if v == 1]

print(Solution().uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour"))
print(Solution().uncommonFromSentences(A = "apple apple", B = "banana"))
print(Solution().uncommonFromSentences(A = "s z z z s", B = "s z ejt"))