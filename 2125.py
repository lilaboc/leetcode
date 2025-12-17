# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        upper = 0
        result = 0
        for i in bank:
            line = i.count('1')
            if line > 0:
                if upper == 0:
                    upper = line
                else:
                    result += upper * line
                    upper = line
        return result





print(Solution().numberOfBeams(["011001","000000","010100","001000"]))
print(Solution().numberOfBeams(["000","111","000"]))

