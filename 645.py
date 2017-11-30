# https://leetcode.com/problems/set-mismatch/description/
from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_num = 0
        s = set()
        duplicate = 0
        for i in nums:
            if i > max_num:
                max_num = i
            if i not in s:
                s.add(i)
            else:
                duplicate = i
        missing = max_num + 1
        for i in xrange(1, max_num):
            if i not in s:
                missing = i
                break
        return [duplicate, missing]


#print(Solution().findErrorNums([1,2,2,4]))
