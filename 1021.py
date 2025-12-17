# https://leetcode.com/problems/remove-outermost-parentheses/description/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        now = ''
        count = 0
        for i in s:
            if i == '(':
                count += 1
            else:
                count -= 1
            now += i
            if count == 0:
                result.append(now[1:-1])
                now = ''

        return "".join(result)


print(Solution().removeOuterParentheses('(()())(())'))
print(Solution().removeOuterParentheses('(()())(())(()(()))'))
print(Solution().removeOuterParentheses('()()'))

