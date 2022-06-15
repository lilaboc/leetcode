# https://leetcode.com/problems/percentage-of-letter-in-string/

from collections import Counter
import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l = len(s)
        s = Counter(s)
        if letter not in s:
            return 0
        return math.floor(s[letter] * 100 / l)



print(Solution().percentageLetter("foobar", "o"))
print(Solution().percentageLetter("jjjj", "k"))
