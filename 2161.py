# https://leetcode.com/problems/partition-array-according-to-given-pivot/
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equals = []
        larger = []
        for i in nums:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                larger.append(i)
            else:
                equals.append(i)
        return smaller + equals + larger


print(Solution().pivotArray([9,12,5,10,14,3,10], 10))

