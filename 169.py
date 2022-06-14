# https://leetcode.com/problems/majority-element/
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c.keys():
            if c[i] > len(nums) / 2:
                return i


print(Solution().majorityElement([2,2,1,1,1,2,2]))