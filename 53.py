# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrent = nums[0]
        maxGlobal = nums[0]
        for i in nums[1:]:
            maxCurrent = max(maxCurrent + i, i)
            if maxCurrent > maxGlobal:
                maxGlobal = maxCurrent
        return maxGlobal




print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
