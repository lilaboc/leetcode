# https://leetcode.com/problems/find-center-of-star-graph/
from collections import Counter
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter()
        for edge in edges:
            c[edge[0]] += 1
            c[edge[1]] += 1
        return c.most_common(1)[0][0]


print(Solution().findCenter([[1,2],[2,3],[4,2]]))
