# https://leetcode.com/problems/hand-of-straights/description/
from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        for _ in range(int(len(hand) / groupSize)):
            start = min(c.keys())
            for i in range(start, start + groupSize):
                if i not in c:
                    return False
                else:
                    c[i] -= 1
                    if c[i] == 0:
                        c.pop(i)
        return True




print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(Solution().isNStraightHand([3,2,1,2,3,4,3,4,5,9,10,11], 3))
print(Solution().isNStraightHand([3,2,1,2,3,4,3,4,5,9,10,12], 3))
print(Solution().isNStraightHand([1,2,3,4,5], 4))
