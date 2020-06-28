# https://leetcode.com/problems/valid-mountain-array/

from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        prev = A[0]
        increased = False
        decreased = False
        for i in A[1:]:
            if i > prev:
                increase = True
            elif i < prev:
                increase = False
            else:
                return False

            if not increased and increase:
                increased = True
            if increase and decreased:
                return False
            elif not increase and not decreased:
                decreased = True
            prev = i
        return increased and decreased 
                




print(Solution().validMountainArray([2,1]))
print(Solution().validMountainArray([3,5, 5]))
print(Solution().validMountainArray([0,3,2,1]))