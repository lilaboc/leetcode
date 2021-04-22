# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = 0
        for i in range(len(A)):
            if A[i] > peak:
                peak = A[i]
            elif A[i] < peak:
                return i - 1

print(Solution().peakIndexInMountainArray([0, 1, 0]))
print(Solution().peakIndexInMountainArray([0,2,1,0]))
                    
