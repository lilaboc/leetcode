# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        a = Counter(nums1)
        b = Counter(nums2)
        result = []
        for i in a.keys():
            if b.has_key(i):
                for o in xrange(b[i] if a[i] > b[i] else a[i]):
                    result.append(i)
        return result
