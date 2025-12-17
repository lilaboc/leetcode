# https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for i in nums1:
            for j in nums2:
                if i % (j * k) == 0:
                    count += 1
        return count

print(Solution().numberOfPairs( [1,3,4],  [1,3,4], 1))
print(Solution().numberOfPairs( [1,2,4,12],  [2,4], 2))
