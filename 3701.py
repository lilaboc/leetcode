# https://leetcode.com/problems/compute-alternating-sum/description/
from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        for idx, value in enumerate(nums):
            if idx % 2 ==0:
                result += value
            else:
                result -= value
        return result




print(Solution().alternatingSum([1,3,5,7]))
