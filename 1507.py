# https://leetcode.com/problems/reformat-date/

import re

class Solution:
    def __init__(self):
        self.months = lambda x: str(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(x) + 1).rjust(2, "0")
        self.days = lambda x: re.search('\d+', x, re.I|re.M|re.S).group(0).rjust(2, '0')

    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        return f"{year}-{self.months(month)}-{self.days(day)}"


print(Solution().reformatDate("20th Oct 2052"))
print(Solution().reformatDate("6th Jun 1933"))