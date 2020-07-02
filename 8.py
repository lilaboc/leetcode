# https://leetcode.com/problems/string-to-integer-atoi/

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        m = re.search('^[+-]?\d+', str.lstrip())
        if not m:
            return 0
        else:
            n = int(m.group(0))
            if n < -2147483648:
                n = -2147483648
            if n > 2147483648:
                n = 2147483647
            return n
        # except:
        #     return 0
        

print(Solution().myAtoi("42"))
print(Solution().myAtoi("         -42"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))
        
print(Solution().myAtoi("3.14159"))