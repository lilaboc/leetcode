# https://leetcode.com/problems/separate-the-digits-in-an-array/
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for num in nums:
            for n in str(num):
                yield int(n)


print(Solution().separateDigits([13,25,83,77]))