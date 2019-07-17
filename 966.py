# https://leetcode.com/problems/vowel-spellchecker/
from typing import List
import re
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_matches = set(wordlist)
        d = {}
        for i in wordlist:
            if i.lower() not in d:
                d[i.lower()] = i
            word = re.sub('[aeiou]', '_', i.lower())
            if word not in d:
                d[word] = i


        def find(word):
            if word in exact_matches:
                return word
            elif word.lower() in d:
                return d[word.lower()]
            else:
                word = re.sub('[aeiou]', '_', word.lower())
                if word in d:
                    return d[word]
            return ""
        return [find(query) for query in queries]


print(Solution().spellchecker( ["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
