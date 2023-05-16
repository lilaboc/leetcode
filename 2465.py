# https://leetcode.com/problems/number-of-distinct-averages/
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        while len(nums) != 0:
            s.add((nums.pop(0) + nums.pop()) / 2)
        return len(s)


print(Solution().distinctAverages([4,1,4,0,3,5]))
