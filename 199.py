# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            current = root
            rows = [[root]]
            q1 = []
            q2 = []
            q1.append(root)
            while True:
                for i in q1:
                    if i.left:
                        q2.append(i.left)
                    if i.right:
                        q2.append(i.right)
                if len(q2) == 0:
                    break
                else:
                    q1 = q2
                    rows.append(q2)
                    q2 = []
            result = []
            for i in rows:
                result.append(i[-1].val)
        return result



                


