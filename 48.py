# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(int(n / 2)):
            for col in range(row, n - row - 1):
                #pos = [(row, col), (col, n - row - 1), (n - row - 1, n - col -1), (n - col - 1, row)]
                matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row] = matrix[n - col - 1][row], matrix[row][col], matrix[col][n - row - 1], matrix[n - row - 1][n - col - 1]



# a = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# Solution().rotate(a)
# print(a)
a = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
Solution().rotate(a)
print(a)