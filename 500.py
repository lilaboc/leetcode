# https://leetcode.com/problems/keyboard-row/#/description
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for word in words:
            for row in rows:
                if all([o in row for o in word.lower()]):
                    result.append(word)
                    break
        return result

#print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
