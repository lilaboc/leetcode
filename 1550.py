# https://leetcode.com/problems/three-consecutive-odds/

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 == 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False


print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print(Solution().threeConsecutiveOdds([2,6,4,1]))