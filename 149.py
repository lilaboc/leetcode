# https://leetcode.com/problems/max-points-on-a-line/

from typing import List
from collections import defaultdict
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
                


        d = defaultdict(lambda : defaultdict(lambda: []))

        for i in range(len(points)):
            for o in range(len(points)):
                if i != o:
                    slope = self.slope(points[i], points[o])
                    d[i][slope].append(o)
        m = 0
        print(d)


        for i in d.keys():
            for slope in d[i].keys():
                if len(d[i][slope]) + 1 > m:
                    m = len(d[i][slope]) + 1
        return m 
    

    def slope(self, a, b):
        if a[0] == b[0]:
            return math.inf
        else:
            return (b[1] - a[1]) / (b[0] - a[0])


# print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
# print(Solution().maxPoints([[1,1],[2,2],[3,3]]))
# print(Solution().maxPoints([[0,0],[1,1],[0,0]]))
# print(Solution().maxPoints([[1,1],[2,1],[2,2],[1,4],[3,3]]))
print(Solution().maxPoints([[1,1],[1,1],[2,2],[2,2]]))
