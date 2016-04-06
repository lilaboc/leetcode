# https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        if len(strs) != len(pattern):
            return False
        dict = {}
        for i,o in zip(pattern, strs):
            if dict.has_key(i) and dict[i] != o:
                return False
            else:
                dict[i] = o
        return len(dict.values()) == len(set(dict.values()))

#print Solution().wordPattern('abba', 'dog cat cat dog')
#print Solution().wordPattern('abba', 'dog dog dog dog')
