# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = head
        current = head
        while True:
            if current != prev:
                if current.val == prev.val:
                    prev.next = current.next
                else:
                    prev = current
            if current == None or current.next == None:
                break
            current = current.next
        return head

