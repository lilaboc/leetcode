# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        else:
            result = set()
            self.sum(root, 0, result)
            return sum in result

    def sum(self, node, val, result):
        if node.left == None and node.right == None:
            result.add(val + node.val)
        else:
            val += node.val
            if node.left != None:
                self.sum(node.left, val, result)
            if node.right != None:
                self.sum(node.right, val, result)
