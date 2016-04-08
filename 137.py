# https://leetcode.com/problems/single-number-ii/
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return Counter(nums).most_common()[-1][0]

#print Solution().singleNumber([1, 2, 1, 3, 2, 5]) 
