# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {}
        for i, v in enumerate(nums):
            d[v] = i
        if target in d:
            return d[target]
        else:
            return -1

