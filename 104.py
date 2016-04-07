# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            level = 1
            q1 = []
            q2 = []
            q1.append(root)
            while True:
                current = q1.pop()
                if current.left:
                    q2.append(current.left)
                if current.right:
                    q2.append(current.right)
                if len(q1) == 0:
                    if len(q2) == 0:
                        return level
                    else:
                        level += 1
                        q1, q2 = q2, q1



