# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) <= 1:
            return 0
        now = prices[-1]
        for p in prices[-1::-1]:
            if p < now:
                profit += now - p
            now = p
        return profit


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
