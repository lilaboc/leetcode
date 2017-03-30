# https://leetcode.com/problems/first-unique-character-in-a-string/#/description
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        for i in xrange(len(s)):
            if counter[s[i]] == 1:
                return i
        else:
            return -1

#print Solution().firstUniqChar("leetcode")
#print Solution().firstUniqChar("loveleetcode")
