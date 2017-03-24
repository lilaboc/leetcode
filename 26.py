#https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            length = 1
            last = nums[0]
            result = 1
            for i in xrange(1, len(nums)):
                #print nums[i]
                if nums[i] != last:
                    length += 1
                    last = nums[i]
                    nums[result] = nums[i]
                    result += 1
        nums = nums[:length]
        return length

#nums = [1,1,1,2]
#print Solution().removeDuplicates(nums) 
#print nums
