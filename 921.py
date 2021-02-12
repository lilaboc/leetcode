# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        left = 0
        for i in S:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    count += 1
        return count + left


print(Solution().minAddToMakeValid("()("))
print(Solution().minAddToMakeValid("((("))
print(Solution().minAddToMakeValid("()"))
print(Solution().minAddToMakeValid("()))(("))