# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
import string
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        upper = string.ascii_uppercase
        r = []
        for l in upper[upper.find(start[0]): upper.find(end[0]) + 1]:
            for n in range(int(start[1]), int(end[1]) + 1):
                r.append(l + str(n))
        return r


print(Solution().cellsInRange("K1:L2"))
print(Solution().cellsInRange("A1:F1"))
