# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        result_head = None
        l1_ended = False
        l2_ended = False
        incre = False
        while True:
            if not l1_ended and not l2_ended:
                val = l1.val + l2.val
            elif l1_ended:
                val = l2.val
            elif l2_ended:
                val = l1.val
            if incre:
                val += 1
            if val > 9:
                val = val % 10
                incre = True
            else:
                incre = False
            if result == None:
                result = ListNode(val)
                result_head = result
            else:
                result.next = ListNode(val)
                result = result.next
            if l1.next == None:
                l1_ended = True
            if l2.next == None:
                l2_ended = True
            if l1_ended and l2_ended:
                if incre:
                    result.next = ListNode(1)
                break
            else:
                if not l1_ended:
                    l1 = l1.next
                if not l2_ended:
                    l2 = l2.next
        return result_head 

#a = ListNode(2)
#b = ListNode(4)
#c = ListNode(3)
#a.next = b
#b.next = c
#
#e = ListNode(5)
#f = ListNode(6)
#g = ListNode(4)
#h = ListNode(1)
#e.next = f
#f.next = g
#g.next = h
#head = Solution().addTwoNumbers(a, e)
#while True:
#    print head.val
#    if head.next == None:
#        break
#    else:
#        head = head.next
