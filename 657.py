# https://leetcode.com/problems/judge-route-circle/description/
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        now = [0, 0]
        for i in moves:
            if i == 'U':
                now[1] += 1
            elif i == 'D':
                now[1] -= 1
            elif i == 'L':
                now[0] -= 1
            else:
                now[0] += 1
        return now == [0, 0]

#print Solution().judgeCircle("UD")
#print Solution().judgeCircle("LL")
