# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __repr__(self):
         r = []
         a = self
         while True:
             r.append(a.val)
             if a.next is None:
                 break
             a = a.next
         return r.__repr__()

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.toHead(self.toList(head)[::-1])


    def toList(self, head):
        r = []
        while head is not None:
            r.append(head.val)
            head = head.next
        return r

    def toHead(self, r):
        if len(r) == 0:
            return None
        head = ListNode(r[0])
        now = head
        for i in r[1:]:
            now.next = ListNode(i)
            now = now.next
        return head

