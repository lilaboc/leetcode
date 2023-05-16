# https://leetcode.com/problems/sort-the-people/
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for n, h in zip(names, heights):
            d[h] = n
        return [d[i] for i in sorted(d.keys(), reverse=True)]


print(Solution().sortPeople(["Mary","John","Emma"],  [180,165,170]))