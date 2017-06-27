#https://leetcode.com/problems/reshape-the-matrix/#/description

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_list = [item for sublist in nums for item in sublist]
        if r * c != len(flat_list):
            return nums
        else:
            result = []
            for i in xrange(r):
                #print i * c
                #print (i + 1) * c
                result.append(flat_list[ i * c: (i  + 1) * c])
            return result


#print Solution().matrixReshape([[1,2], [3,4]], 1, 4)
#print Solution().matrixReshape([[1,2], [3,4]], 2, 4)
#print Solution().matrixReshape([[1], [2], [3], [4]], 2, 2)

