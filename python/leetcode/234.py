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

    def reverse(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        buf = []
        cur = head
        while cur:
            buf.append(cur)
            cur = cur.next

        newHeader = ListNode(0)
        cur = newHeader
        while len(buf) > 0:
            node = buf.pop(-1)
            node.next = None
            cur.next = node
            cur = cur.next
        return newHeader.next


    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        willReserve = slow.next
        slow.next = None

        reversed = self.reverse(willReserve)

        first = head
        second = reversed
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

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
    mid = sol.isPalindrome(head)
    print(mid)

    head = buildList([1, 2, 2, 1])
    mid = sol.isPalindrome(head)
    print(mid)