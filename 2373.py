# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        result = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                result[x][y] = max(grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3))
        return result



print(Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
