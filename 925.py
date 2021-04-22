# https://leetcode.com/problems/long-pressed-name/

import re
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return True if name == typed or re.match(''.join([f"{i}+" for i in name]), typed) else False

print(Solution().isLongPressedName('alex', 'aaleex'))
print(Solution().isLongPressedName('saeed', 'ssaaedd'))
print(Solution().isLongPressedName('leelee', 'lleeelee'))
print(Solution().isLongPressedName('laiden', 'laiden'))

        
                    
