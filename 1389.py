# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, o in zip(nums, index):
            result.insert(o, i)
        return result


print(Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1]))