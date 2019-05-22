
from typing import List

# Definition for singly-linked list.
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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        div = int(n / 2)
        l1 = self.mergeKLists(lists[:div])
        l2 = self.mergeKLists(lists[div:])
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        cur1 = l1
        cur2 = l2
        cur = head = ListNode(-1)

        has_more = True
        while has_more:
            if cur1 and cur2:
                if cur1.val <= cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            elif cur1:
                cur.next = cur1
                has_more = False
            elif cur2:
                cur.next = cur2
                has_more = False
            else:
                cur.next = None
                has_more = False
        return head.next



if __name__ == '__main__':
    l1 = ListNode(-9)
    l1.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(7)

    l3 = ListNode(15)
    l3.next = ListNode(70)

    s = Solution()
    r = s.mergeKLists([l1, l2, l3])
    print(r)
