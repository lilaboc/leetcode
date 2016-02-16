# https://leetcode.com/problems/add-digits/
# https://en.wikipedia.org/wiki/Digital_root
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num-9*((num-1)/9)
