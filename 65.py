# https://leetcode.com/problems/valid-number/
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return re.match('^\s*[+-]?(\d+(\.\d+)?|\.\d+|\d+\.?)(e[+-]*\d+)?\s*$', s, re.I|re.M|re.S) != None
if False:
    print Solution().isNumber('0') 
    print Solution().isNumber(' 0.1 ') 
    print Solution().isNumber('abc') 
    print Solution().isNumber('1 a') 
    print Solution().isNumber('2e10') 
    print Solution().isNumber('11') 
    print Solution().isNumber('.1') 

