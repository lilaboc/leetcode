# https://leetcode.com/problems/height-checker/
from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                count += 1
        return count


#print(Solution().heightChecker([1,1,4,2,1,3]))
#print(Solution().heightChecker([5,1,2,3,4]))
        