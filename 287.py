# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List

# bloom filter?

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return i
