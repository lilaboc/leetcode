# https://leetcode.com/problems/excel-sheet-column-number/
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        for i in s:
            result = 26 * result + (letters.index(i) + 1) 
        return result
        

#print Solution().titleToNumber('Z')
#print Solution().titleToNumber('AA')
#print Solution().titleToNumber('AB')
#print Solution().titleToNumber('AAA')
