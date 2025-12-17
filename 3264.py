# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m = min(nums)
            for j in range(len(nums)):
                if nums[j] == m:
                    nums[j] *= multiplier
                    break
        return nums



print(Solution().getFinalState([2,1,3,5,6], 5, 2))

