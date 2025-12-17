# https://leetcode.com/problems/count-of-matches-in-tournament/description/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n >= 2:
            if n % 2 == 0:
                count += n / 2
                n /= 2
            else:
                count += (n - 1) / 2
                n -= (n - 1) / 2
        return int(count)

print(Solution().numberOfMatches(7))
print(Solution().numberOfMatches(14))
print(Solution().numberOfMatches(1))

