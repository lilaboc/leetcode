# https://leetcode.com/problems/self-dividing-numbers/
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right + 1):
            for o in str(i):
                o = int(o)
                if o == 0:
                    break
                if i % o != 0:
                    break
            else:
                r.append(i)
        return r


print(Solution().selfDividingNumbers(1, 22))
print(Solution().selfDividingNumbers(47, 85))


