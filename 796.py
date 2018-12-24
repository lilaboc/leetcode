# https://leetcode.com/problems/rotate-string/
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        for i in range(1, len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False


print(Solution().rotateString('abcde', 'cdeab'))
print(Solution().rotateString('abcde', 'abced'))

