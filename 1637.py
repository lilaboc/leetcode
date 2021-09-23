# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = set(point[0] for point in points)
        if len(a) == 1:
            return 0
        a = sorted(a)
        return max([a[i + 1] - a[i] for i in range(0, len(a) - 1, 1)])



# print(Solution().maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
# print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
print(Solution().maxWidthOfVerticalArea([[58,71],[64,41],[96,14],[26,37],[11,67],[84,2],[72,0],[16,95],[74,100],[60,98],[8,45],[6,59],[69,32],[93,12],[26,56],[9,39],[61,84],[54,93],[43,47],[84,40],[95,82],[17,85],[99,41],[96,24],[83,10],[82,62],[26,81],[74,96],[53,0],[11,72],[51,35],[33,3],[33,52],[58,94],[89,92],[54,85]]
))
