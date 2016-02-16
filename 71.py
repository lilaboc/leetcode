# https://leetcode.com/problems/simplify-path/
from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        queue = deque()
        for i in path.split('/'):
            if i == '':
                pass
            else:
                if i == '..' :
                    if len(queue) > 0:
                        queue.pop()
                elif i == '.':
                    pass
                else:
                    queue.append(i)
        result = ''
        if len(queue) == 0:
            return '/'
        while len(queue) > 0:
            result += '/' + queue.popleft()
        return result

#print Solution().simplifyPath("/a/./b/../../c/")
#print Solution().simplifyPath("/home/")
#print Solution().simplifyPath("/home//foo/")
#print Solution().simplifyPath("/../")
            
