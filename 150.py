# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            operators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.div}
            if i in operators:
                right = stack.pop()
                left = stack.pop()
                if i == '/':
                    stack.append(int(operators[i](left, float(right))))
                else:
                    stack.append(operators[i](left, right))
            else:
                stack.append(int(i))
            #print stack
        return stack.pop()

#print Solution().evalRPN(["2", "1", "+", "3", "*"])
#print Solution().evalRPN(["4", "13", "5", "/", "+"])
#print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
