# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        heng = [max(row) for row in grid]
        shu = [0] * len(grid[0])
        for i in range(len(grid[0])):
            shu[i] = max([grid[o][i] for o in range(len(grid))])
        r = 0
        for i in range(len(grid)):
            for o in range(len(grid[0])):
                r += min(heng[i], shu[o]) - grid[i][o]
        return r



print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

