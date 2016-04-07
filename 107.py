# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for binary tree with next pointer.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            current = root
            q1 = []
            q2 = []
            q1.append(root)
            result = [[root.val]]
            while True:
                for i in q1:
                    if i.left:
                        q2.append(i.left)
                    if i.right:
                        q2.append(i.right)
                if len(q2) == 0:
                    break
                else:
                    result.append([o.val for o in q2])
                    q1 = q2
                    q2 = []
            return result[::-1]
