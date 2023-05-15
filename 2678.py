# https://leetcode.com/problems/number-of-senior-citizens/
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for detail in details if int(detail[11: 13]) > 60)



print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(Solution().countSeniors(["1313579440F2036","2921522980M5644"]))
