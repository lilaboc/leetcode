# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/


class Solution:
    def minPartitions(self, n: str) -> int:
        return max((int(i) for i in n))


print(Solution().minPartitions("27346209830709182346"))
