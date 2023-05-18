# https://leetcode.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for row_num in range(len(triangle) - 2, -1, -1):
            row = triangle[row_num]
            for idx in range(len(row)):
                if triangle[row_num + 1][idx] < triangle[row_num + 1][idx + 1]:
                    row[idx] += triangle[row_num + 1][idx]
                else:
                    row[idx] += triangle[row_num + 1][idx + 1]
        return triangle[0][0]


print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))