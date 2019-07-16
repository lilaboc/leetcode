# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        d = deque()
        for i in S:
            if len(d) > 0 and d[-1] == i:
                d.pop()
            else:
                d.append(i)
        return ''.join(d)

print(Solution().removeDuplicates('abbaca'))

            
            

