# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
import string

class Solution:
    def minTimeToType(self, word: str) -> int:
        s = 0
        r = 0
        for i in word:
            t = string.ascii_lowercase.index(i)
            n = abs(s - t)
            if n >= 13:
                n = 26 - n
            r += n + 1
            s = t
        return r

print(Solution().minTimeToType("bza"))
print(Solution().minTimeToType("zjpc"))

