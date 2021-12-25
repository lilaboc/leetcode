# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = 0
        count = 0
        for i in nums:
            if i < target:
                smaller += 1
            elif i == target:
                count += 1
        return [smaller + i for i in range(count)]


print(Solution().targetIndices([1,2,5,2,3], 2))
print(Solution().targetIndices([1,2,5,2,3], 5))

        