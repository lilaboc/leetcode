# https://leetcode.com/problems/sum-of-left-leaves/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.transverse(root, False)
        
    def transverse(self, node, left):
        if node == None:
            return 0
        if left and node.left == None and node.right == None:
            return node.val
        else:
            return self.transverse(node.left, True) + self.transverse(node.right, False)
