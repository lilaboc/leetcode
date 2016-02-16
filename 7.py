# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            s = int('-' + s[-1:0:-1])
        else:
            s = int(s[-1::-1])
        if abs(s) > 2147483647:
            return 0
        return s

#print Solution().reverse(0)
