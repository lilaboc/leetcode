# https://leetcode.com/problems/shuffle-an-array/
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums.copy()
        random.shuffle(nums)
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()