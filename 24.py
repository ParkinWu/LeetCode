# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head
        if not first:
            return None

        second = first.next
        if not second:
            return first

        rest = second.next
        l1 = self.swapPairsInner(first, second)
        l2 = self.swapPairs(rest)
        l1.next = l2
        return second

    def swapPairsInner(self, first: ListNode, second: ListNode) -> ListNode:
        first.next = None
        second.next = first
        return first