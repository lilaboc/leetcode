# https://leetcode.com/problems/keep-multiplying-found-values-by-two/
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            for i in nums:
                if i == original:
                    original *= 2
                    break
            else:
                break
        return original


print(Solution().findFinalValue([5,3,6,1,12], 3))
print(Solution().findFinalValue([2,7,9], 4))
print(Solution().findFinalValue([8,19,4,2,15,3], 2))
