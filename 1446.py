# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        m = 1
        last = s[0]
        current = 1
        for i in s[1:]:
            if i != last:
                if current > m:
                    m = current
                current = 1
            else:
                current += 1
            last = i
        if current > m:
            m = current
        return m


print(Solution().maxPower("abbcccddddeeeeedcba"))
print(Solution().maxPower("hooraaaaaaaaaaay"))
print(Solution().maxPower("j"))
print(Solution().maxPower("jj"))