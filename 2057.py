# https://leetcode.com/problems/smallest-index-with-equal-value/

from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1


print(Solution().smallestEqual([0,1,2]))
print(Solution().smallestEqual([4,3,2,1]))
print(Solution().smallestEqual([1,2,3,4,5,6,7,8,9,0]))
