# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        r = [0] * len(boxes)
        for i, box in enumerate(boxes):
            if box == '1':
                for o in range(len(boxes)):
                    if i != o:
                        r[o] += abs(i - o)
        return r


print(Solution().minOperations("110"))
print(Solution().minOperations("001011"))
