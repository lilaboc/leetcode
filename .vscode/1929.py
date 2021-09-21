# https://leetcode.com/problems/concatenation-of-array/
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r = [1] * 2 * len(nums)
        for i, v in enumerate(nums):
            r[i] = v
            r[i + len(nums)] = v
        return r

print(Solution().getConcatenation([1,2,1]))
        
