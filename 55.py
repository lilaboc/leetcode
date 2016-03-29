# https://leetcode.com/problems/jump-game/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = 0
        end = None
        while True:
            this = nums[cur]
            if end == None:
                end = this
            elif end < cur + this:
                end = cur + this
            if cur == len(nums) - 1:
                return True
            elif cur == end:
                return False
            cur += 1
#print Solution().canJump([2, 3, 1, 1, 4])
#print Solution().canJump([3, 2, 1, 0, 4])
