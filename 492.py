# https://leetcode.com/problems/construct-the-rectangle/#/description
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        root = int(math.ceil(math.sqrt(area)))
        for i in xrange(root, area + 1):
            if area % i == 0:
                return [i, area / i]


#print Solution().constructRectangle(2)
