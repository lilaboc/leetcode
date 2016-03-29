# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'{': '}', '[':']', '(':')'}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) != 0:
                if pairs[stack.pop()] != i:
                    return False
            else:
                return False
        return len(stack) == 0
#print Solution().isValid('()[]{}')
#print Solution().isValid('(]')
