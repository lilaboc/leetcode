# https://leetcode.com/problems/row-with-maximum-ones/
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        best = [0, 0]
        for row_number, row in enumerate(mat):
            count = row.count(1)
            if count > best[1]:
                best = [row_number, count]
        return best


print(Solution().rowAndMaximumOnes([[0,0],[1,1],[0,0]]))
