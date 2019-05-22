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

    def reverseList(self, head: ListNode) -> ListNode:
        first = head
        if not first:
            return None
        rest = first.next
        if not rest:
            return first

        l1 = self.reverseList(rest)
        rest.next = first
        first.next = None
        return l1

    def reverseK(self, head: ListNode, k: int) -> ListNode:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n = n + 1
            if n == k:
                break

        if n < k:
            return head
        return self.reverseList(head)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n = n + 1

        if n < k:
            return head

        # 前k个元素，翻转后 连接到后面

        tail = head
        m = k - 1
        while m > 0:
            tail = tail.next
            m = m - 1
        rest = tail.next
        tail.next = None

        l1 = self.reverseK(head, k)
        l2 = self.reverseKGroup(rest, k)

        head.next = l2

        return l1


if __name__ == '__main__':
    current = ListNode(0)
    head = current
    for i in range(1, 21):
        node = ListNode(i)
        current.next = node
        current = node
    print(head)
    sol = Solution()
    l1 = sol.reverseKGroup(head, 6)
    print(l1)
