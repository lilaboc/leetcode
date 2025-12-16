# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()
        for i in nums:
            if i in seen:
                result.append(i)
                if len(result) == 2:
                    return result
            seen.add(i)
        return result
