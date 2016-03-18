# https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for index, value in enumerate(nums):
            if d.has_key(value):
                if index - d[value] <= k:
                    return True
                else:
                    d[value] = index
            else:
                d[value] = index
        return False

#print Solution().containsNearbyDuplicate([1,2,3,4,1], 2)
#print Solution().containsNearbyDuplicate([1,2,3,4,1], 5)
