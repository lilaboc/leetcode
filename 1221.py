# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        r = 0
        for i in s:
            if i == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                r += 1
        return r

print(Solution().balancedStringSplit("RLLLLRRRLR"))

