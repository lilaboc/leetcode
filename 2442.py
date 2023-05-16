# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            s.add(int(str(i)[::-1]))
        return len(s)

print(Solution().countDistinctIntegers([1,13,10,12,31]))