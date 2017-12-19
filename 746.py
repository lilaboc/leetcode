# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in xrange(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        else:
            return min(cost[0], cost[1])

print Solution().minCostClimbingStairs([10, 15, 20])
print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
