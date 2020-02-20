# Definition for singly-linked list.

from typing import List
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ""
        current = self
        s = s + str(current.val)
        while current.next:
            current = current.next
            s = s + " -> "
            s = s + str(current.val)
        return s


def buildList(list: List[int]) -> ListNode:
    if len(list) == 0:
        return None
    head = ListNode(0)
    cur = head
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next

    return head.next

class Solution(object):

    def reverse(self, head: ListNode) -> ListNode:
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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        needReverse = slow.next
        slow.next = None

        reversed = self.reverse(needReverse)

        cur = head
        insert = reversed
        while insert:
            tmp = cur.next
            cur.next = insert
            insertNext = insert.next
            insert.next = None
            insert.next = tmp
            insert = insertNext
            cur = cur.next.next


if __name__ == '__main__':
    sol = Solution()
    head = buildList([1,2,3,4,5,6])
    sol.reorderList(head)
    print(head)

    head = buildList([1, 2, 3, 4, 5])
    sol.reorderList(head)
    print(head)

    head = buildList([])
    sol.reorderList(head)
    print(head)

    # head = buildList([1, 2, 3, 4, 5, 6])
    # print(head)
    # sol = Solution()
    # l = sol.reorderList(head)
    # print(l)