# Definition for singly-linked list.
from typing import List

class ListNode:
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


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        cur = newHead
        while cur and cur.next:
            next = cur.next
            if next.val is val:
                tmp = next.next
                cur.next = tmp
            else:
                cur = cur.next
        return newHead.next


def buildList(list: List[int]) -> ListNode:
    if len(list) == 0:
        return None
    head = ListNode(0)
    cur = head
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next

    return head.next


if __name__ == '__main__':
    sol = Solution()
    head = buildList([1, 2, 3, 4, 5, 6])
    mid = sol.removeElements(head, 3)
    print(mid)

    head = buildList([1, 2, 3, 4, 5, 6])
    mid = sol.removeElements(head, 6)
    print(mid)

    head = buildList([1, 2, 3, 4, 5, 6])
    mid = sol.removeElements(head, 1)
    print(mid)

    head = buildList([1, 1])
    mid = sol.removeElements(head, 1)
    print(mid)