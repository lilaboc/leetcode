# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = Counter()
        l = Counter()
        for m in matches:
            w[m[0]] += 1
            l[m[1]] += 1
        r1 = [i for i in sorted(w.keys()) if i not in l]
        r2 = [i for i in sorted(l.keys()) if l[i] == 1]
        return [r1, r2]


print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(Solution().findWinners([[2,3],[1,3],[5,4],[6,4]]))

