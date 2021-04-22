# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            count = 0
            for j in nums:
                if i != j and i> j:
                    count += 1
            result.append(count)
        return result
            



print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
        