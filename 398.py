# https://leetcode.com/problems/random-pick-index/

from typing import List
from collections import defaultdict
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.d = defaultdict(lambda: [])
        for idx, val in enumerate(nums):
            self.d[val].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3,3])
print(obj.pick(3))