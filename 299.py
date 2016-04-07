# https://leetcode.com/problems/bulls-and-cows/
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow_secret = ''
        guess_secret = ''
        for i, o in zip(secret, guess):
            if i == o:
                bull += 1
            else:
                cow_secret += i
                guess_secret += o
        cow = sum((Counter(cow_secret) & Counter(guess_secret)).values())
        return "{0}A{1}B".format(bull, cow)
