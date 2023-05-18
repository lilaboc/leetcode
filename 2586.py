# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
from typing import List

def isvowel(s):
    return s[0] in 'aeiou' and s[-1] in 'aeiou'

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum([1 for i in words[left: right + 1] if isvowel(i)])


print(Solution().vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))