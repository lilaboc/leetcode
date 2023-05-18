# https://leetcode.com/problems/most-frequent-even-element/description/
from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter([i for i in nums if i % 2 == 0])
        most = c.most_common()
        if len(most) == 0:
            return -1
        return sorted([i[0] for i in most if i[1] == most[0][1]])[0]


print(Solution().mostFrequentEven([0,1,2,2,4,4,1]))