# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        now = None
        start = None
        d = {}
        for i,v in enumerate(nums):
            if now is None:
                now = v
                start = i
            if now != v:
                d[now] = [start, i - 1]
                now = v
                start = i
        d[now] = [start, len(nums) - 1]
        if target in d:
            return d[target]
        else:
            return [-1, -1]

# print(Solution().searchRange([5,7,7,8,8,10], 8))
# print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([1], 1))

