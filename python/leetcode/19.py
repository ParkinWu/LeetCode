# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur1 = head
        cur2 = head
        i = n
        while i and cur2.next:
            cur2 = cur2.next
            i = i - 1

        if i > 0:
            return cur1.next

        while cur2.next:
            cur2 = cur2.next
            cur1 = cur1.next

        cur1.next = cur1.next.next
        return head

