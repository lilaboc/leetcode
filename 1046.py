# https://leetcode.com/problems/last-stone-weight/


from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a, b = stones[-2:]
            c = b - a
            if c == 0:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [c]
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

print(Solution().lastStoneWeight([2,7,4,1,8,1]))