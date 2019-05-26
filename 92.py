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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        cur_pos = 0
        cur = new_head
        stack = []
        while cur.next or len(stack) > 0:
            cur_pos = cur_pos + 1
            if cur_pos > n:
                tmp = cur.next
                while len(stack) > 0:
                    last = stack.pop(-1)
                    cur.next = last
                    cur = cur.next
                cur.next = tmp
                break
            elif cur_pos >= m:
                x = cur.next
                cur.next = cur.next.next
                x.next = None
                stack.append(x)
            else:
                cur = cur.next
        return new_head.next


if __name__ == '__main__':
    head = buildList([1, 2, 3, 4, 5, 6, 7, 8])
    print(head)
    sol = Solution()
    l = sol.reverseBetween(head, 2, 6)
    print(l)

    head = buildList([3, 5])
    print(head)
    sol = Solution()
    l = sol.reverseBetween(head, 1, 2)
    print(l)

    head = buildList([])
    print(head)
    sol = Solution()
    l = sol.reverseBetween(head, 0, 0)
    print(l)

    head = buildList([1])
    print(head)
    sol = Solution()
    l = sol.reverseBetween(head, 1, 1)
    print(l)