# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        mm = [[None, None]]
        m3 = None
        for i in xrange(0, len(nums)):
            deal = False
            for j in xrange(0, len(mm)):
                m1 = mm[j][0]
                m2 = mm[j][1]
                if m1 == None or m2 == None and m1 > nums[i]:
                    #print m1, m2
                    mm[j][0] = nums[i]
                    mm[j][1] = None
                    deal = False
                    break
                elif m1 < nums[i]:
                    if m2 == None or m2 > nums[i]:
                        mm[j][1] = nums[i]
                        deal = False
                        break;
                    elif m2 < nums[i]:
                        m3 = nums[i]
                        #print m1
                        #print m2
                        #print m3
                        return True
                if m2 != None and nums[i] < m1:
                    deal = True
            if deal:
                tmp = [nums[i], None]
                mm.append(tmp)
                

        return False


#print Solution().increasingTriplet([1, 0, 0, 1])
