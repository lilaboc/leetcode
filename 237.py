# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next != None:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None

#a = ListNode(1)
#b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)
#a.next = b
#b.next = c
#c.next = d
#Solution().deleteNode(c)
#head = a
#while head.next != None:
#    print head.val
#    head = head.next

