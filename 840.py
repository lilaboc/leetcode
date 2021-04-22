# https://leetcode.com/problems/magic-squares-in-grid/

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        count = 0
        self.nums = set(range(1, 10))
        for x in range(len(grid) - 2):
            for y in range(len(grid[0]) - 2):
                if self.ismagic(x, y):
                    count += 1
        return count

    def ismagic(self, x, y):
        nums = set()
        for i in range(x, x + 3):
            for o in range(y, y + 3):
                nums.add(self.grid[i][o])
        if nums != self.nums:
            return False 
        row1 = sum(self.grid[x][y:y+3])
        row2 = sum(self.grid[x + 1][y:y+3])
        row3 = sum(self.grid[x + 2][y:y+3])
        col1 = sum([i[y] for i in self.grid[x:x+3]])
        col2 = sum([i[y + 1] for i in self.grid[x:x+3]])
        col3 = sum([i[y + 2] for i in self.grid[x:x+3]])
        diagnol1 = sum([self.grid[x][y], self.grid[x+1][y+1], self.grid[x+2][y+2]])
        diagnol2 = sum([self.grid[x][y+2], self.grid[x+1][y+1], self.grid[x+2][y]])
        if row1==row2==row3==col1==col2==col3==diagnol1==diagnol2:
            return True
        else:
            return False

print(Solution().numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]]))
        