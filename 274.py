# https://leetcode.com/problems/h-index/
from collections import defaultdict
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        length = len(citations)
        for i in citations:
            for o in xrange(i + 1):
                d[o] += 1
        #print d
        for i in xrange(length, -1, -1):
            if d[i] >= i:
                return i

#print Solution().hIndex([3, 0, 6, 1, 5])
#print Solution().hIndex([0])
