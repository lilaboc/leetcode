# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        if len(nodes) % 2 == 0:
            return False
        else:
            gap = 0
            for index, value in enumerate(nodes):
                if value == '#':
                    if index == 0 and len(nodes) == 1:
                        return True
                    elif index == 0 and len(nodes) != 1:
                        return False
                    else:
                        gap -= 1
                else:
                    if index == 0:
                        gap += 2
                    else:
                        gap += 1
                if gap == 0 and index != len(nodes) - 1:
                    return False
                if gap < 0:
                    return False
            return gap == 0

#print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
#print Solution().isValidSerialization("1,#")
#print Solution().isValidSerialization("9,#,#,1")
 
#print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
#print Solution().isValidSerialization("7,2,#,2,#,#,#,6,#")
