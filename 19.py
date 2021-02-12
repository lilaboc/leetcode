# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        while head != None:
            l.append(head)
            head = head.next
        if len(l) - n == 0:
            del l[0]
        elif len(l) - n - 1 >= 0 and len(l) - n + 1 < len(l):
            l[-n - 1].next = l[-n + 1]
        else:
            l[- n - 1].next = None
        if len(l) >= 1:
            return l[0]
        else:
            return None


head = None
now = None

for i in range(1, 3):
    l = ListNode(i)
    if not head:
        head = l
        now = l
    else:
        now.next = l
        now = now.next


head = Solution().removeNthFromEnd(head, 1)
while head:
    print(head.val)
    head = head.next

    
