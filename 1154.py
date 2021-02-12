# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        import datetime
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        return date.timetuple().tm_yday


print(Solution().dayOfYear("2019-01-09"))