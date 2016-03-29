# https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        m = re.search('\s*(?P<last>[a-zA-Z]+)$', s.strip(), re.I|re.M|re.S)
        if m:
            return len(m.group('last'))
        else:
            return 0
