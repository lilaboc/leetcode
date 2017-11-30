# https://leetcode.com/problems/max-area-of-island/description/
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        result = []
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                result.append(self.travel(x, y, grid, seen))
        return max(result)




    def travel(self, x, y, grid, seen):
        if grid[x][y] != 0 and (x, y) not in seen:
            width = len(grid)
            height = len(grid[0])
            seen.add((x, y))
            points = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
            points = filter(lambda x:  x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < height and grid[x[0]][x[1]] == 1 and (x[0],x[1]) not in seen, points)
            #print seen
            #print points
            return 1 + sum([self.travel(i[0], i[1], grid, seen) for i in points])
        else:
            return 0
        

#
#print Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]])
#
#
#
#print Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
