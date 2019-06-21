# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        cur = newList
        carry = 0
        while l1 or l2:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            sum = l1.val + l2.val + carry
            carry = sum // 10
            rest = sum % 10
            node = ListNode(rest)
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if carry > 0:
            cur.next = ListNode(carry)
        return newList.next




if __name__ == '__main__':
    s = Solution()
    l1 = buildList([2, 4, 3])
    l2 = buildList([5, 6, 4])
    l3 = s.addTwoNumbers(l1, l2)
    print(l3)

    l1 = buildList([5])
    l2 = buildList([5])
    l3 = s.addTwoNumbers(l1, l2)
    print(l3)
