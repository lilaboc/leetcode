# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
from collections import Counter
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = {v: k for k, v in Counter(A).items()}
        return counter[len(A) / 2]

print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
