# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        while curA is not curB:
            if curA is None:
                curA = headB
            else:
                curA = curA.next

            if curB is None:
                curB = headA
            else:
                curB = curB.next
        return curA

