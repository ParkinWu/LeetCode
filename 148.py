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


def buildList(list: List[int]) -> ListNode:
    if len(list) == 0:
        return None
    head = ListNode(0)
    cur = head
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next

    return head.next

class Solution:

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        newList = ListNode(0)
        cur = newList
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        return newList.next


    def mergeSort(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None

        l1 = self.mergeSort(first)
        l2 = self.mergeSort(second)

        return self.merge(l1, l2)

    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)


if __name__ == '__main__':
    sol = Solution()
    head = buildList([1,3,5,4,2,8])
    sol.sortList(head)
    print(head)