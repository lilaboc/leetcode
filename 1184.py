# https://leetcode.com/problems/distance-between-bus-stops/

from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start >= destination:
            start, destination = destination, start
        return min(sum(distance[start: destination]), sum(distance[destination:] + distance[:start]))




print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 3))
        