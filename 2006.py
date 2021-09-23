# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        r = 0
        for i in range(len(nums) - 1):
            for o in range(i, len(nums)):
                if abs(nums[i] - nums[o]) == k:
                    r += 1
        return r


print(Solution().countKDifference([3,2,1,5,4], 2))