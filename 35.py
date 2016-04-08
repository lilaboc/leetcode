# https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)
        else:
            left = 0 
            right = len(nums) - 1
            while True:
                middle = (left + right) / 2
                if right - left == 1:
                    return left + 1
                if nums[middle] < target:
                    left = middle
                if nums[middle] > target:
                    right = middle
                if nums[middle] == target:
                    return middle

#print Solution().searchInsert([1,3,5,6], 5)
#print Solution().searchInsert([1,3,5,6], 2)
#print Solution().searchInsert([1,3,5,6], 7)
#print Solution().searchInsert([1,3,5,6], 0)
#print Solution().searchInsert([1, 3], 1)
#print Solution().searchInsert([1, 3], 3)
#print Solution().searchInsert([1], 2)
