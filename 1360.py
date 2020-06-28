# https://leetcode.com/problems/number-of-days-between-two-dates/

import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        return abs((date1 - date2).days)
        

print(Solution().daysBetweenDates("2019-06-29", "2019-06-30"))
print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))