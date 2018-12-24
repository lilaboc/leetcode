# https://leetcode.com/problems/largest-number-greater-than-twice-of-others/description/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        second_largest = -1
        pos = 0
        for i in xrange(1, len(nums)):
            num = nums[i]
            if num > largest:
                second_largest = largest
                largest = num
                pos = i
            elif num > second_largest:
                second_largest = num
        print largest, second_largest
        if largest >= second_largest * 2:
            return pos
        else:
            return -1

#print(Solution().dominantIndex([3, 6, 1, 0]))
#print(Solution().dominantIndex([1, 2, 3, 4]))
#print(Solution().dominantIndex([1, 0, 0, 0]))
