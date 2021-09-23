# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        r = []
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                r.append(i)
        return r
