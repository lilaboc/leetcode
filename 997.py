# https://leetcode-cn.com/problems/find-the-town-judge/
from typing import List
from collections import Counter
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        to_trust = Counter()
        trusted = Counter()
        for i in trust:
            to_trust[i[1]] += 1
            trusted[i[0]] += 1
         
        J = None
        for i in to_trust.keys():
            if to_trust[i] == N - 1:
                if J == None:
                    J = i
                else:
                    return -1
        if J == None or trusted[J] != 0:
            return -1
        return J


print(Solution().findJudge(1, []))
# print(Solution().findJudge(2, [[1,2]]))
# print(Solution().findJudge(3, [[1,3],[2,3],[3,1]]))
# print(Solution().findJudge(2, [[1,2],[2,3]]))
# print(Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))