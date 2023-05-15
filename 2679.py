# https://leetcode.com/problems/sum-in-a-matrix/
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(num, reverse=True) for num in nums]
        score = 0
        for i in range(len(nums[0])):
            score += max(num[i] for num in nums)
        return score


print(Solution().matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))