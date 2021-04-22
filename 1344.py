# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ahour = (hour + minutes / 60) * 30 
        aminute = (minutes / 60) * 360
        if ahour >= 360:
            ahour -= 360
        if ahour > aminute:
            angle = ahour - aminute
        else:
            angle = aminute - ahour
        if angle > 180:
            angle = 360 - angle
        return angle

# print(Solution().angleClock(12, 30))
# print(Solution().angleClock(3, 30))
# print(Solution().angleClock(3, 15))
# print(Solution().angleClock(12, 0))
# print(Solution().angleClock(1, 57))