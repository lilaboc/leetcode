# https://leetcode.com/problems/find-indices-of-stable-mountains/description/
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        before = 0
        result = []
        for i in range(len(height) - 1):
            if height[i] > threshold:
                result.append(i + 1)
        return result




print(Solution().stableMountains([1,2,3,4,5], 2))
print(Solution().stableMountains([10,1,10,1,10], 3))
print(Solution().stableMountains([10,1,10,1,10], 10))
