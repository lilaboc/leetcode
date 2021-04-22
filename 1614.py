# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        mdepth = 0
        for i in s:
            if i == '(':
                depth += 1
                if depth > mdepth:
                    mdepth = depth
            elif i == ')':
                depth -= 1
        return mdepth
        
print(Solution().maxDepth('(1+(2*3)+((8)/4))+1'))
print(Solution().maxDepth("(1)+((2))+(((3)))"))
print(Solution().maxDepth("1+(2*3)/(2-1)"))

