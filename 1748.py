# https://leetcode.com/problems/sum-of-unique-elements/

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum((k for k, v in Counter(nums).items() if v == 1))



print(Solution().sumOfUnique([1,2,3,2]))