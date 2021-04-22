# https://leetcode.com/problems/powerful-integers/
import math
from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        def get_max(v):
            if v == 1:
                return 1
            return math.ceil(math.log(bound, v))
        max_x, max_y = get_max(x), get_max(y)
        for i in range(max_x + 1):
            for o in range(max_y + 1):
                num = pow(x, i) + pow(y, o) 
                if num <= bound:
                    result.add(num)
        return list(result)

print(Solution().powerfulIntegers(2, 1, 10))
print(Solution().powerfulIntegers(2, 3, 10))
print(Solution().powerfulIntegers(3, 5, 15))
                    
