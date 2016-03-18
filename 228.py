# https://leetcode.com/problems/summary-ranges/
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        start = None
        prev = None
        result = []
        for i in nums:
            if start == None:
                start = i 
            elif i - prev != 1:
                if start == prev:
                    result.append("{0}".format(start))
                else:
                    result.append("{0}->{1}".format(start, prev))
                start = i
            prev = i
        if start == prev:
            result.append("{0}".format(start))
        else:
            result.append("{0}->{1}".format(start, prev))
        return result
#print Solution().summaryRanges([0,1,2,4,5,7]) 
#print Solution().summaryRanges([0,1,2,4,5,7,8]) 
