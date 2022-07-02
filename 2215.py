# https://leetcode.com/problems/find-the-difference-of-two-arrays/
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [[i for i in s1 if i not in s2], [i for i in s2 if i not in s1]]


print(Solution().findDifference([1,2,3,3], [1,1,2,2]))


