# https://leetcode.com/problems/remove-linked-list-elements/
from typing import Optional


# Definition for singly-linked list.
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
    # Definition for singly-linked list.
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return self.toHead([i for i in self.toList(head) if i != val])

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

print(Solution().removeElements(listToLists([1,2,6,3,4,5,6]), 6))