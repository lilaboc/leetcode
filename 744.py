# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in xrange(len(letters)):
            if letters[i] > target:
                return letters[i]
        else:
            return letters[0]


