# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List
from collections import defaultdict

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for x, y in zip(startTime, endTime):
            if queryTime >= x and queryTime <= y:
                count += 1
        return count


print(Solution().busyStudent([1,2,3], [3,2,7], 2))