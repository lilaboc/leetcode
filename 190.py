# https://leetcode.com/problems/reverse-bits/
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print "08b".format(n)[::-1]
        return int('{0:032b}'.format(n)[::-1], 2)
#print Solution().reverseBits(43261596)
