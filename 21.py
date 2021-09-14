# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional


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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
            prev = head
        else:
            head = ListNode(l2.val)
            l2 = l2.next
            prev = head
        while l1 is not None or l2 is not None:
            if l1 is None or ((l1 is not None and l2 is not None) and l2.val <= l1.val):
                prev.next = ListNode(l2.val)
                prev = prev.next
                l2 = l2.next
            elif l2 is None or ((l1 is not None and l2 is not None) and l2.val > l1.val):
                prev.next = ListNode(l1.val)
                prev = prev.next
                l1 = l1.next
        return head





def listToLists(nums):
    head = None
    prev = None
    for num in nums:
        node = ListNode(num)
        if head is None:
            head = node
            prev = node
        else:
            prev.next = node
            prev = node
    return head





print(Solution().mergeTwoLists(listToLists([1, 2, 4]), listToLists([1, 3, 4])))
# print(Solution().mergeTwoLists(listToLists([]), listToLists([])))
# print(Solution().mergeTwoLists(listToLists([]), listToLists([0])))
# print(listToLists([0]))









