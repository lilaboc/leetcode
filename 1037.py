# https://leetcode.com/problems/valid-boomerang/
from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        return self.angle(points[1], points[0]) != self.angle(points[1], points[2])

    def angle(self, A, B):
        if A[0] == B[0]:
            return None
        return (B[1] - A[1]) / (B[0] - A[0])



print(Solution().isBoomerang([[0,1],[1,0],[1,1]]))
#print(Solution().isBoomerang([[0,1],[0,2],[1,2]]))
# print(Solution().isBoomerang([[1,1],[2,3],[3,2]]))
# print(Solution().isBoomerang([[1,1],[2,2],[3,3]]))