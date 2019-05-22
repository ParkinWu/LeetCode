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

    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    print(r)
