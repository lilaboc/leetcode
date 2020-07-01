# https://leetcode.com/problems/day-of-the-week/

import datetime

class Solution:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = datetime.datetime(year, month, day)
        return self.days[d.weekday()]


print(Solution().dayOfTheWeek(15, 8 , 1993))

