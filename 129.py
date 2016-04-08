# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.sum(root, '')



    def sum(self, node, val):
        if node.left == None and node.right == None:
            return int(val + str(node.val))
        else:
            val += str(node.val)
            result = 0
            if node.left != None:
                result += self.sum(node.left, val)
            if node.right != None:
                result += self.sum(node.right, val)
            return result
