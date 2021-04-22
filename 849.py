# https://leetcode.com/problems/maximize-distance-to-closest-person/

from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        empty = []
        length = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if len(empty) == 0:
                    empty.append(length)
                elif length != 0:
                    empty.append(length)
                length = 0
            else:
                length += 1
        empty.append(length)
        if len(empty) > 2:
            return max([empty[0], int((max(empty[1:-1]) + 1) / 2), empty[-1]])
        else:
            return max(empty[0], empty[1])
        

        
        # return max([empty[0], int((max(empty[1:-1]) + 1) / 2), empty[-1]])

        



print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(Solution().maxDistToClosest([1,0,0,0]))