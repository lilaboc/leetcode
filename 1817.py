# https://leetcode.com/problems/finding-the-users-active-minutes/description/
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = {}
        for uid, minute in logs:
            if uid not in d:
                d[uid] = set()
            d[uid].add(minute)
        result = [0] * k
        for v in d.values():
            result[len(v) - 1] += 1
        return result




print(Solution().findingUsersActiveMinutes( [[0,5],[1,2],[0,2],[0,5],[1,3]], 5))
print(Solution().findingUsersActiveMinutes( [[1,1],[2,2],[2,3]], 4))
