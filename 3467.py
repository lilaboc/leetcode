# https://leetcode.com/problems/transform-array-by-parity/description/
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        even = 0
        for i in nums:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return [0] * even + [1] * odd


print(Solution().transformArray([4,3,2,1]))
print(Solution().transformArray([1,5,1,4,2]))
