# https://leetcode.com/problems/find-common-characters/
from typing import List
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = Counter(A[0])
        for i in A[1:]:
            c = Counter(i)
            for k in list(d.keys()):
                if k not in c:
                    del d[k]
            for k, v in c.items():
                if k in d:
                    d[k] = min(d[k], v)
        return list(d.elements())
print(Solution().commonChars( ["bella","label","roller"]))
                    
