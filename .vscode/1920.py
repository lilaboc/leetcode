# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        r = [0] * len(nums)
        for i in range(len(nums)):
            r[i] = nums[nums[i]]
        return r