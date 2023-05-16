# https://leetcode.com/problems/rearrange-array-elements-by-sign/
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        r = []
        for p, n in zip(positive, negative):
            r.append(p)
            r.append(n)
        return r
