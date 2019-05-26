# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        map = {}
        index = 0
        current = head
        while current is not None:
            key = str(id(current))
            if map.__contains__(key):
                return current
            map[key] = index
            index = index + 1
            current = current.next
        return None