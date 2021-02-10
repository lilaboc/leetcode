# https://leetcode.com/problems/number-of-good-pairs/

from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(lambda : [])
        for i in range(len(nums)):
            d[nums[i]].append(i)
        count = 0
        for i in d:
            count += sum(range(len(d[i])))
        return count


print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))

        