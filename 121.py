# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = None
        max_profit = 0
        for i in prices:
            if lowest is None:
                lowest = i
            else:
                if i - lowest > max_profit:
                    max_profit = i - lowest
                if i < lowest:
                    lowest = i
        return max_profit




print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
