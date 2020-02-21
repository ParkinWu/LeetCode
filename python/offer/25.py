#
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
#
# 0 <= 链表长度 <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        node = ListNode(0)
        cur = node
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1.next
                l1.next = None
                cur.next = l1
                l1 = tmp
            else:
                tmp = l2.next
                l2.next = None
                cur.next = l2
                l2 = tmp
            cur = cur.next

        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        return node.next
