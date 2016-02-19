# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(0, len(nums) - 1):
            for o in xrange(i + 1, len(nums)):
                if nums[i] + nums[o] == target:
                    return [i, o]


#print Solution().twoSum([2, 7, 11, 15], 9)
#print Solution().twoSum([0, 0], 0)

        

        
