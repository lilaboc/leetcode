# https://leetcode.com/problems/reverse-degree-of-a-string/description/

class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((idx + 1) * (ord('z') - ord(v) + 1) for idx, v in enumerate(s))



print(Solution().reverseDegree('abc'))
print(Solution().reverseDegree('zaza'))

