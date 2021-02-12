# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import List
from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        d = defaultdict(lambda : [])
        for i in arr:
            d[str(bin(i))[2:].count('1')].append(i)

        result = []
        for i in sorted(d.keys()):
            for o in sorted(d[i]):
                result.append(o)
        return result


# print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]
))
