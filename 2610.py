# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        r = []
        c = Counter(nums)
        while len(c) > 0:
            row = [i for i in list(c.keys())]
            for i in row:
                c[i] -= 1
                if c[i] == 0:
                    c.pop(i)
            r.append(row)
        return r

print(Solution().findMatrix([1,3,4,1,2,3,1]))

