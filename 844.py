# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.p(S) == self.p(T)


    def p(self, S: str) -> str:
        r = [''] * len(S)
        p = 0
        for i in S:
            if i == '#':
                if p > 0:
                    p -= 1
            else:
                r[p] = i
                p += 1
        return ''.join(r[:p])


        
Solution().backspaceCompare('a##c', '#a#c')