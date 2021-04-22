# https://leetcode.com/problems/duplicate-zeros/
from collections import deque
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        q = deque()
        for i in range(len(arr)):
            if len(q) > 0:
                item = q.popleft()
                q.append(arr[i])
                if arr[i] == 0:
                    q.append(0)
                arr[i] = item
            elif arr[i] == 0:
                    q.append(0)


a = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(a)
print(a)
