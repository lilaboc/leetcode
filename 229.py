# https://leetcode.com/problems/majority-element-ii/
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k, v in c.items() if v > int(len(nums) / 3)]