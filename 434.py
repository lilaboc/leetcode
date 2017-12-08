# https://leetcode.com/problems/number-of-segments-in-a-string/description/
import re
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(filter(lambda x: len(x) != 0, re.split('\s+',s)))

#print Solution().countSegments('')
        


