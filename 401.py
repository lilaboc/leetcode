# https://leetcode.com/problems/binary-watch/description/
import itertools 
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        lists = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        pos = range(10)
        result = []
        for i in itertools.combinations(pos, num):
            h = 0
            m = 0
            for o in i:
                if o < 4:
                    h += lists[o]
                else:
                    m += lists[o]
            if h <= 11 and m <= 59:
                result.append("{}:{:0>2}".format(h, m))
        return result


        
#print Solution().readBinaryWatch(2)
