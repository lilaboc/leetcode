# https://leetcode.com/problems/decompress-run-length-encoded-list/
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums) // 2) :
            r.extend([nums[i * 2 + 1]] * nums[i * 2])
        return r


print(Solution().decompressRLElist([1, 2, 3, 4]))
print(Solution().decompressRLElist([1, 1, 2, 3]))
