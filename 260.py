# https://leetcode.com/problems/single-number-iii/
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [i[0] for i in Counter(nums).most_common()[-2:]]

#print Solution().singleNumber([1, 2, 1, 3, 2, 5]) 
