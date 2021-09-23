# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [i + extraCandies >= m for i in candies]


print(Solution().kidsWithCandies([2,3,5,1,3], 3))