# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from typing import List
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        # nums.sort()
        c = Counter(nums)

        for _ in range(int(len(nums) / k)):
            s = sorted(c.keys())[0]
            for o in range(k):
                n = s + o
                if c[n] > 0:
                    c[n] -= 1
                    if c[n] == 0:
                        del c[n]
                else:
                    return False
        return True

print(Solution().isPossibleDivide([1,2,3,3,4,4,5,6], 4))
print(Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3))
print(Solution().isPossibleDivide([1,2,3,4], 3))