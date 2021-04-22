# https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i, o in zip(nums[:n], nums[n:]):
            result.append(i)
            result.append(o)
        return result



print(Solution().shuffle([2,5,1,3,4,7], 3))
print(Solution().shuffle([1,2,3,4,4,3,2,1], 4))
print(Solution().shuffle([1,1,2,2], 2))