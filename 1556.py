# https://leetcode.com/problems/thousand-separator/


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        return '.'.join(l(len(s) % 3, s))



def l(start, s):
    if start != 0:
        yield s[:start]
    for i in range(start, len(s), 3):
        yield s[i: i+ 3]

Solution().thousandSeparator(123456789)
Solution().thousandSeparator(1234567890)
        