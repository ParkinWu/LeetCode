# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5

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
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_header = ListNode(0)
        more_header = ListNode(0)

        less_p = less_header
        more_p = more_header

        while head is not None:
            if head.val < x:
                less_p.next = head
                less_p = head
            else:
                more_p.next = head
                more_p = head
            head = head.next
        less_p.next = more_header.next
        more_p.next = None

        return less_header.next




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
    head = buildList([1, 4, 3])
    print(head)
    sol = Solution()
    l = sol.partition(head, 4)
    print(l)