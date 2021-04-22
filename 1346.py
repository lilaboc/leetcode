# https://leetcode.com/problems/check-if-n-and-its-double-exist/

from typing import List
from collections import Counter
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for i in arr:
            if i == 0 and c[i] >= 2:
                return True

            if i != 0 and i * 2 in c:
                return True
        return False
        