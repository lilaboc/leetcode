# https://leetcode.com/problems/delete-greatest-value-in-each-row/
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid = [sorted(num, reverse=True) for num in grid]
        score = 0
        for i in range(len(grid[0])):
            score += max(num[i] for num in grid)
        return score


print(Solution().deleteGreatestValue([[1,2,4],[3,3,1]]))