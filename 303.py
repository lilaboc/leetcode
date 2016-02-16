# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []
        tsum = 0
        for index, val in enumerate(self.nums):
            tsum += val
            self.sums.append(tsum)

        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return self.sums[j] - self.sums[i] + self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
#numArray = NumArray([1,2,3])
#print numArray.sumRange(0, 1)
#print numArray.sumRange(1, 2)
