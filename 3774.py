# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return sum(nums[-k:]) - sum(nums[:k])


print(Solution().absDifference([1, 2, 3, 4], 2))
print(Solution().absDifference([100], 1))
