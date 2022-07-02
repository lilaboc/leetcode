# https://leetcode.com/problems/strong-password-checker-ii/

import string

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        upper = False
        lower = False
        digit = False
        special = False
        prev = ''
        adjacent = False
        for i in password:
            if i == prev:
                adjacent = True
            prev = i
            if i in string.ascii_uppercase:
                upper = True
            elif i in string.ascii_lowercase:
                lower = True
            elif i in string.digits:
                digit = True
            elif i in '!@#$%^&*()-+':
                special = True
        if upper and lower and digit and special and not adjacent:
            return True
        return False


print(Solution().strongPasswordCheckerII("IloveLe3tcode!"))
print(Solution().strongPasswordCheckerII("Me+You--IsMyDream"))
