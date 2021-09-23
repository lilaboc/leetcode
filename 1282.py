# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(lambda: [])
        r = []
        for i, v in enumerate(groupSizes):
            d[v].append(i)
        for i, v in d.items():
            for o in range(0, len(v), i):
                r.append(v[o: o + i])
        return r


print(Solution().groupThePeople([3,3,3,3,3,1,3]))
print(Solution().groupThePeople([2,1,3,3,3,2]))


