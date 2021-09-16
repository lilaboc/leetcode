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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.toHead(self.digits_to_list(self.node_to_digit(l1) + self.node_to_digit(l2)))

    def digits_to_list(self, num):
        r = []
        while True:
            num, m = divmod(num, 10)
            r.append(m)
            if num == 0:
                break
        return r[::-1]

    def node_to_digit(self, head):
        r = 0
        while head is not None:
            r = r * 10 + head.val
            head = head.next
        return r

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

# print(Solution().addTwoNumbers(listToLists([7, 2, 4, 3]), listToLists([5, 6, 4])))
print(Solution().addTwoNumbers(listToLists([2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9]), listToLists([5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9])))



# print(digits_to_list(101))
