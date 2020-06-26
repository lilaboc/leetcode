# https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        marea = 0
        a = 0
        b = len(height) - 1
        while a < b:
            area = min(height[a], height[b]) * (b - a)
            if area > marea:
                marea = area
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return marea



print(Solution().maxArea( [1,8,6,2,5,4,8,3,7]))
       