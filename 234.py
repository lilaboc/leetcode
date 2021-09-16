# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r = self.toList(head)
        if len(r) % 2 == 0:
            return r[:int(len(r) / 2)] == r[int(len(r) / 2):][::-1]
        else:
            return r[:int(len(r) / 2)] == r[int(len(r) / 2) + 1:][::-1]


    def toList(self, head):
        r = []
        while head is not None:
            r.append(head.val)
            head = head.next
        return r

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

print(Solution().isPalindrome(listToLists([1, 2, 2, 1])))