# https://leetcode.com/problems/flipping-an-image/

from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        invert = lambda x : 1 if x == 0 else 0
        for row in A:
            length = len(row)
            for i in range(int(length / 2)):
                row[i], row[length - i - 1] = row[length - i - 1], row[i]
            for i in range(length):
                row[i] = invert(row[i])
        return A

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
