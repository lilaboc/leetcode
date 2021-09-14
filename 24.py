# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import Optional
import itertools

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        r = []
        a = self
        while a is not None:
            r.append(a.val)
            a = a.next
        return r.__repr__()

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pairs = []
        now = head
        count = 0
        odd = []
        even = []
        while now is not None:
            if count % 2 == 0:
                even.append(now)
            else:
                odd.append(now)
            count += 1
            now = now.next
        if len(even) == 0:
            return None
        else:
            head = None
            r = []
            for a, b in itertools.zip_longest(odd, even):
                if a is not None:
                    a.next = None
                    r.append(a)
                if b is not None:
                    b.next = None
                    r.append(b)
            if len(r) == 1:
                return r[0]
            for i in range(0, len(r) - 1):
                if head is None:
                    head = r[i]
                r[i].next = r[i + 1]
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


# print(Solution().swapPairs(listToLists([1,2,3,4])))
print(Solution().swapPairs(listToLists([1])))
