# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for k,v in enumerate(A):
            A[k] = abs(v)
        A.sort()
        for k,v in enumerate(A):
            A[k] = pow(v, 2)
        return A
            


        # return [pow(o, 2) for o in sorted([abs(i) for i in A])]


print(Solution().sortedSquares([-7,-3,2,3,11]))