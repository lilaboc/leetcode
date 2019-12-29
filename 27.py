# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)
        


nums = [3,2,2,3]
print(Solution().removeElement(nums, 3))
print(nums)