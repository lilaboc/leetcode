# https://leetcode.com/problems/crawler-log-folder/
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                depth -= 1
                if depth < 0:
                    depth = 0
            elif log == './':
                pass
            else:
                depth += 1
        return depth
                    
            



print(Solution().minOperations(["d1/","d2/","../","d21/","./"]))
print(Solution().minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(Solution().minOperations( ["d1/","../","../","../"]))
        