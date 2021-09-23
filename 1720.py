# https://leetcode.com/problems/decode-xored-array/
from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = [first]
        now = first
        for i in encoded:
            now = now ^ i
            r.append(now)
        return r

print(Solution().decode([6,2,7,3], 4))