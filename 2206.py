# https://leetcode.com/problems/divide-array-into-equal-pairs/
from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(True if value % 2 == 0 else False for value in Counter(nums).values())


print(Solution().divideArray([3,2,3,2,2,2]))
print(Solution().divideArray([1, 2, 3, 4]))
