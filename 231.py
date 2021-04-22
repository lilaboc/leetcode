# https://leetcode.com/problems/power-of-two/submissions/
import math
class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        while n >= 2:
            n /= 2
        return n == 1

# print(Solution().isPowerOfTwo(3))
# print(Solution().isPowerOfTwo(8))
        