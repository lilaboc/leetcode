# https://leetcode.com/problems/reformat-phone-number/

import re
from typing import List


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.sub("[- ]", '', number)
        if len(number) <= 4:
            return '-'.join(self._format_last_4(number))
        else:
            remains = len(number) % 3
            if remains == 0:
                last = len(number) - 3
            elif remains == 1:
                last = len(number) - 4
            else:
                last = len(number) - 2
            r = []
            for i in range(0, last, 3):
                r.append(number[i: i + 3])
            r.extend(self._format_last_4(number[last:]))
            return '-'.join(r)

    def _format_last_4(self, s : str) -> List[str]:
        if len(s) == 2 or len(s) == 3:
            return [s]
        else:
            return [s[:2], s[2:]]


print(Solution().reformatNumber('1-23-45 6'))
print(Solution().reformatNumber("123 4-567"))
print(Solution().reformatNumber("123 4-5678"))
print(Solution().reformatNumber('12'))
print(Solution().reformatNumber("--17-5 229 35-39475 "))

