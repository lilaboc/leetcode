# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, o in enumerate(s):
            d[o] = i
        pos = 0
        start = 0
        high = -1
        r = []
        while pos != len(s):
            if high == -1:
                start = pos
            if d[s[pos]] > high:
                high = d[s[pos]]
            if high == pos:
                r.append(high - start + 1)
                high = -1
            pos += 1
        return r


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))


