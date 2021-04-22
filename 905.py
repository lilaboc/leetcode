# https://leetcode.com/problems/sort-array-by-parity/
from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0] 

print(Solution().sortArrayByParity([3, 1, 2, 4]))
                    
