# https://leetcode.com/problems/number-of-zero-filled-subarrays/
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        r = 0
        count = 0
        for i in nums:
            if i == 0:
                count += 1
            elif count != 0:
                r += sum(range(count + 1))
                count = 0
        if count != 0:
            r += sum(range(count + 1))
        return r


# print(Solution().zeroFilledSubarray([1,3,0,0,2,0,0,4]))
# print(Solution().zeroFilledSubarray([0,0,0,2,0,0]))
# print(Solution().zeroFilledSubarray([0,1,0,0,1,0,0,0]))
print(Solution().zeroFilledSubarray([0]))
