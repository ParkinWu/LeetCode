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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = head
        if not first:
            return None

        second = first.next
        if not second:
            return first

        if first.val == second.val:
            while second and first.val == second.val:
                second = second.next
            return self.deleteDuplicates(second)
        else:
            next = self.deleteDuplicates(second)
            first.next = next
            return first





if __name__ == '__main__':
    current = ListNode(0)
    head = current
    for i in range(1, 21):
        node1 = ListNode(i)
        node2 = ListNode(i)
        node1.next = node2
        current.next = node1
        current = node2
    current.next = ListNode(21)
    current = current.next
    current.next = ListNode(22)
    print(head)
    sol = Solution()
    l1 = sol.deleteDuplicates(head)
    print(l1)




