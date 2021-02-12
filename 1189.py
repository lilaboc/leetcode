# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter

class Solution:
    def __init__(self):
        self.d = Counter("balloon")
        self.chars = "balon"

    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        count = 0
        while True:
            c.subtract(self.d)
            for i in self.chars:
                if c[i] < 0:
                    return count
            count += 1
        return count
                


        



print(Solution().maxNumberOfBalloons("loonbalxballpoon"))