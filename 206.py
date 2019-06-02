# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        buffer = []
        while cur:
            buffer.append(cur)
            cur = cur.next

        newHead = ListNode(0)
        cur = newHead
        while len(buffer) > 0:
            node = buffer.pop(-1)
            node.next = None
            cur.next = node
            cur = cur.next
        return newHead.next