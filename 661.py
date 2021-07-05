# https://leetcode.com/problems/image-smoother/description/
import copy
import math
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = copy.deepcopy(M)
        for x in xrange(len(M)):
            for y in xrange(len(M[0])):
                c = 0
                s = 0
                points = [point for point in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)] if point[0] >= 0 and point[0] < len(M) and point[1] >= 0 and point[1] < len(M[0])]
                for xv, yv in points:
                    s += M[xv][yv] 
                    c += 1
                result[x][y] = s / c
        return result
    



#print Solution().imageSmoother([[1,1,1], [1,0,1], [1,1,1]])
#print Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
