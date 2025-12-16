# https://leetcode.com/problems/find-closest-person/description/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_steps = abs(x - z)
        y_steps = abs(y - z)
        if x_steps < y_steps:
            return 1
        elif x_steps > y_steps:
            return 2
        else:
            return 0


print(Solution().findClosest(2, 7, 4))
print(Solution().findClosest(2, 5, 6))
print(Solution().findClosest(1, 5, 3))

