# https://leetcode.com/problems/convert-the-temperature/
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.00]


print(Solution().convertTemperature(36.5))
print(Solution().convertTemperature(122.11))
