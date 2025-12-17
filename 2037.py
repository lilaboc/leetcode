# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum((abs(i - v) for i, v in zip(sorted(seats), sorted(students))))



print(Solution().minMovesToSeat([12,14,19,19,12], [19,2,17,20,7]))