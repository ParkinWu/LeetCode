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
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)
        even = ListNode(0)

        cur_odd = odd
        cur_even = even
        cur = head
        count = 0
        while cur:
            next = cur.next
            cur.next = None
            if count % 2 is 1:
                cur_odd.next = cur
                cur_odd = cur_odd.next
            else:
                cur_even.next = cur
                cur_even = cur_even.next
            count = count + 1
            cur = next
        cur_even.next = odd.next
        return even.next

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
    l = sol.oddEvenList(head)
    print(l)