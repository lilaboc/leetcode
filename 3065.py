# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in nums:
            if i < k:
                count += 1
        return count
