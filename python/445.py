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
    def numberFromList(self, head: ListNode) -> int:
        cur = head
        sum = 0
        while cur:
            sum = sum * 10 + cur.val
            cur = cur.next
        return sum

    def listFromNumber(self, num: int) -> ListNode:
        if num == 0:
            return ListNode(0)

        nums = []
        while num > 0:
            val = num % 10
            num = num // 10
            nums.append(ListNode(val))

        head = ListNode(0)
        cur = head
        while len(nums) > 0:
            l = nums.pop(-1)
            cur.next = l
            cur = cur.next
        return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.numberFromList(l1)
        num2 = self.numberFromList(l2)
        sum = num1 + num2
        return self.listFromNumber(sum)

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
    list1 = buildList([1, 2, 3, 4, 5])
    list2 = buildList([2, 3, 4, 5])
    sum = sol.addTwoNumbers(list1, list2)
    print(sum)
