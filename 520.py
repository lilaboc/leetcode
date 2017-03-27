# https://leetcode.com/problems/detect-capital/#/description
import string
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '':
            return False
        all_capital = all([i in string.uppercase for i in word])
        all_lowercase = all([i in string.lowercase for i in word])
        first_capital = word[0] in string.uppercase and len(word) > 1 and all([i in string.lowercase for i in word[1:]])
        return all_capital or all_lowercase or first_capital



        

#print Solution().detectCapitalUse("USA")
#print Solution().detectCapitalUse("FlaG")
