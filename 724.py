# https://leetcode.com/problems/find-pivot-index/

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        t = sum(nums)
        head = 0
        for i in range(len(nums)):
            if head  == t - head - nums[i]:
                return i
            head += nums[i]
        return -1
    

# print(Solution().pivotIndex([1,7,3,6,5,6]))
# print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([-1,-1,-1,0,1,1]))
            

