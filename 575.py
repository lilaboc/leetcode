# https://leetcode.com/problems/distribute-candies/#/description

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = len(set(candies))
        if kinds <= len(candies) / 2:
            return kinds
        else:
            return len(candies) / 2

print Solution().distributeCandies([1,1,2,2,3,3])
print Solution().distributeCandies([1,1,2,3])
