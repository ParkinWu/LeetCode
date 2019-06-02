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
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        return slow


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
    mid = sol.middleNode(head)
    print(mid)

    head = buildList([1, 2, 3, 4, 5])
    mid = sol.middleNode(head)
    print(mid)