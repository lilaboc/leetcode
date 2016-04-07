# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right == None:
            return True
        if (left != None and right == None) or (left == None and right != None):
            return False
        return left.val == right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        
