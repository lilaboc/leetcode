# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum = 0
        count = 0
        for i in range(1, n + 1):
            if i not in banned:
                sum += i
                if sum > maxSum:
                    return count
                else:
                    count += 1
        return count

# print(Solution().maxCount([11], 7, 50))
print(Solution().maxCount([1,6,5], 5, 6))
