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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        list = []
        left = head
        while left:
            x = left
            list.append(x)
            left = left.next
            x.next = None

        n = len(list)
        index = math.ceil(n / 2.0) - 1
        tail = n - 1 - index

        

        firstIndex = 0
        tailIndex = n - 1
        new = ListNode(0)
        cur = new
        while firstIndex < tailIndex:
            first = list[firstIndex]
            second = list[tailIndex]
            second.next = None
            first.next = second
            cur.next = first
            cur = cur.next.next
            firstIndex = firstIndex + 1
            tailIndex = tailIndex - 1


        if firstIndex is tailIndex:
            cur.next = list[firstIndex]
        return new.next


if __name__ == '__main__':
    head = buildList([1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1])
    print(head)
    sol = Solution()
    l = sol.reorderList(head)
    print(l)

    # head = buildList([1, 2, 3, 4, 5, 6])
    # print(head)
    # sol = Solution()
    # l = sol.reorderList(head)
    # print(l)