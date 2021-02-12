# https://leetcode.com/problems/shuffle-string/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = [''] * len(s)
        for x, y in zip(s, indices):
            a[y] = x
        return ''.join(a)


print(Solution().restoreString('codeleet', [4,5,6,7,0,2,1,3]))