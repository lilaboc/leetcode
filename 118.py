# https://leetcode.com/problems/pascals-triangle/

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            if i <= 2:
                result.append([1] * i)
            else:
                l = result[i - 2]
                result.append([1] + [l[o - 1] + l[o] for o in range(1, i - 1)] + [1])
        return result



print(Solution().generate(5))