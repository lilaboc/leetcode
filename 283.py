# https://leetcode.com/problems/move-zeroes/
from collections import deque
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        queue = deque()
        for index, val in enumerate(nums):
            if val == 0:
                queue.append(index)
            else:
                if len(queue) != 0:
                    nums[queue.popleft()] = val
                    queue.append(index)
        while len(queue) != 0:
            nums[queue.popleft()] = 0

#nums = [0, 1, 0, 3, 12]
#Solution().moveZeroes(nums)
#print nums
#nums = [0, 0, 0, 3, 12]
#Solution().moveZeroes(nums)
#print nums
