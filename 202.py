# https://leetcode.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            n = self.cal(n)
            print n
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)

    def cal(self, n):
        digits = map(int, list(str(n)))
        return sum(map(lambda x: x * x, digits))
#print Solution().isHappy(19)
