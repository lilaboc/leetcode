# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        return [i for i in range(1, n + 1) if i not in s]


print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))