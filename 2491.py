# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
from collections import Counter
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        if sum(skill) % (len(skill) / 2) != 0:
            return -1
        target = int(sum(skill) / (len(skill) / 2))
        c = Counter(skill)
        result = 0
        for i in skill:
            if len(c) == 0:
                break
            o = target - i
            if i in c and o in c:
                for m in [i, o]:
                    c[m] -= 1
                    if c[m] == 0:
                        c.pop(m)
                result += i * o
        if len(c) > 0:
            return -1
        return result



# print(Solution().dividePlayers([2,1,5,2]))
print(Solution().dividePlayers([5,3,7,1]))
# print(Solution().dividePlayers([2,4,1,3]))
# print(Solution().dividePlayers([3,2,5,1,3,4]))
# print(Solution().dividePlayers([3,4]))
# print(Solution().dividePlayers([1,1,2,3]))
