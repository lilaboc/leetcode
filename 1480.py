# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [None] * len(nums)
        for i, v in enumerate(nums):
            if i == 0:
                sums[i] = v
            else:
                sums[i] = sums[i - 1] + v
        return sums

#print(Solution().runningSum([1,2,3,4]))

