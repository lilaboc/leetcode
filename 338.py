# https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return ["{0:b}".format(i).count('1') for i in xrange(num + 1)]
        
