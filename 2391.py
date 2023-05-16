# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        kinds = "MPG"
        t = 0
        for kind in kinds:
            stop = 0
            for idx, v in enumerate(garbage[::-1]):
                if kind in v:
                    stop = len(garbage) - idx - 1
                    break
            t += sum(travel[:stop])
            t += sum([g.count(kind) for g in garbage])
        return t


print(Solution().garbageCollection(["G","P","GP","GG"], [2, 4, 3]))
print(Solution().garbageCollection(["MMM","PGM","GP"], [3, 10]))


