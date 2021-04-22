# https://leetcode.com/problems/rank-transform-of-an-array/

from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        s = sorted(arr)
        p = s[0]
        r = 1
        d = {}
        d[p] = r
        for i in s[1:]:
            if p != i:
                r += 1
            d[i] = r
            p = i
        return [d[i] for i in arr]
            
                


print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))