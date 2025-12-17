# https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        result[0] = deck[0]
        pos = 1
        for v in deck[1:]:
            found = False
            while True:
                if result[pos] == 0:
                    if not found:
                        found = True
                    else:
                        result[pos] = v
                        break
                pos += 1
                if pos == len(result):
                    pos = 0
        return result






print(Solution().deckRevealedIncreasing([17,13,11,2,3,5,7]))
print(Solution().deckRevealedIncreasing([1, 10000]))
