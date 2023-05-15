# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        s = set(nums)
        for i in range(m):
            if i not in s:
                return i
        return m + 1


print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))