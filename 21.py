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
        newList = ListNode(0)
        cur = newList
        while l1 and l2:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
                tmp.next = None
                cur.next = tmp
            else:
                tmp = l2
                l2 = l2.next
                tmp.next = None
                cur.next = tmp
            cur = cur.next

        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        return newList.next


if __name__ == '__main__':
    l1 = ListNode(-9)
    l1.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(7)

    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    print(r)
