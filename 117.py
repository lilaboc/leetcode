# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            current = root
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
                    for index in xrange(len(q2)):
                        if index < len(q2) - 1:
                            q2[index].next = q2[index + 1]
                    q2[-1].next = None
                    q1 = q2
                    q2 = []
