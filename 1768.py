# https://leetcode.com/problems/merge-strings-alternately/

import itertools

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = []
        for a, b in itertools.zip_longest(word1, word2):
            if a:
                r.append(a)
            if b:
                r.append(b)
        return "".join(r)


print(Solution().mergeAlternately("ab", "pqrs"))
