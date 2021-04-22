# https://leetcode.com/problems/sort-the-matrix-diagonally/

from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        if row == 1:
            return mat
        col = len(mat[0])
        starts = []
        for i in range(row):
            starts.append([i, 0])
        for i in range(1, col):
            starts.append([0, i])
        # print(starts)
        for i in starts:
            x, y = i[0], i[1]
            pos = []
            while x < row and y < col:
                pos.append([x, y])
                x += 1
                y += 1
            for i, o in zip (pos ,(sorted([mat[i[0]][i[1]] for i in pos]))):
                mat[i[0]][i[1]] = o
            # print(pos)
        return mat
                




print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
