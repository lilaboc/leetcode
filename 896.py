# https://leetcode.com/problems/monotonic-array/
from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        prev = A[0]
        direction = None
        for i in A[1:]:
            if i > prev:
                nd = "D"
            elif i < prev:
                nd = "I"
            else:
                continue
            if direction == None:
                direction = nd
            elif direction != nd:
                return False
            prev = i
        return True


print(Solution().isMonotonic([1,2,2,3]))
print(Solution().isMonotonic([1,3,2]))
print(Solution().isMonotonic([1,1,1]))


