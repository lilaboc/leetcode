# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Queue import Queue
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = Queue()
        if not root:
            return []
        current = root
        result = []
        stack = []
        while True:
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                current = current.left
            else:
                if len(stack) == 0:
                    break
                else:
                    current = stack.pop()
        return result
