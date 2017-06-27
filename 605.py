# https://leetcode.com/problems/can-place-flowers/#/description
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        count = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
        for i in xrange(1, len(flowerbed) - 2):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
                
        if count >= n:
            return True
        else:
            return False

#print Solution().canPlaceFlowers([1,0,0,0,1], 1)
#print Solution().canPlaceFlowers([1,0,0,0,1], 2)
