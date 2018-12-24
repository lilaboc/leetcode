# https://leetcode.com/problems/shortest-completing-word/
from collections import Counter
import string
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        words.sort(key = lambda s: len(s))
        plate = Counter(''.join([i.lower() for i in licensePlate if i in string.ascii_letters]))
        for i in words:
            counter = Counter(i.lower())
            for k, v in plate.items():
                if k not in counter or counter[k] < v:
                    break
            else:
                return i


#print(Solution().shortestCompletingWord( "GrC8950", ["measure","other","every","base","according","level","meeting","none","marriage","rest"]))
