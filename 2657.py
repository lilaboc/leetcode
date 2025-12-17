# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa = set()
        sb = set()
        result = []
        for i in range(len(A)):
            sa.add(A[i])
            sb.add(B[i])
            result.append(len(sa& sb))
        return result





print(Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(Solution().findThePrefixCommonArray([2,3,1], [3,1,2]))
