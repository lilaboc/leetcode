# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
from typing import List

def diff(a, b):
    if len(a) != len(b):
        return False
    count = 0
    for i, o in zip(a, b):
        if i != o:
            count += 1
    return count <= 2


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        r = []
        for query in queries:
            for word in dictionary:
                if diff(query, word):
                    r.append(query)
                    break
        return r



print(Solution().twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"]))