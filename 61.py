# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # 链表长度
        n = 0
        cur = head
        tail = head
        while cur:
            if not cur.next:
                tail = cur
            cur = cur.next
            n = n + 1

        if n <= 1:
            return head

        tail.next = head

        step = n - ((k % n) + 1)
        cur = head
        while step > 0:
            cur = cur.next
            step = step - 1
        new_head = cur.next
        cur.next = None
        return new_head