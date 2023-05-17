# https://leetcode.com/problems/adding-spaces-to-a-string/
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        r = []
        spaces = set(spaces)
        for idx, v in enumerate(s):
            if idx in spaces:
                r.append(' ')
            r.append(v)
        return ''.join(r)


print(Solution().addSpaces("icodeinpython", [1,5,7,9]))