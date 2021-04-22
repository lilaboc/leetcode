# https://leetcode.com/problems/reformat-the-string/

import string
import itertools 

class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        for i in s:
            if i in string.digits:
                digits.append(i)
            else:
                letters.append(i)
        if abs(len(digits) - len(letters)) > 1:
            return ""
        else:
            if len(digits) >= len(letters):
                a, b = digits, letters
            else:
                a, b = letters, digits
            result = ''
            for x, y in itertools.zip_longest(a, b):
                if x != None:
                    result += x 
                if y != None:
                    result += y 
            return result


print(Solution().reformat("covid2019"))
print(Solution().reformat("ab123"))
                


        

