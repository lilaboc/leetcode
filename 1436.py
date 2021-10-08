# https://leetcode.com/problems/destination-city/
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = set()
        s = set()
        for i in paths:
            s.add(i[0])
            d.add(i[1])
        return (d - s).pop()


print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
