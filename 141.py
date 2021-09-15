# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = head
        b = head
        while True:
            try:
                a = a.next
                b = b.next
                b = b.next
                if a == b:
                    return True
                if a is None or b is None:
                    return False
            except AttributeError:
                return False

