# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None

        def buildDST(head, tail) -> TreeNode:
            if head is tail:
                return None

            slow = head
            fast = head
            while fast.next is not tail and fast.next.next is not tail:
                slow = slow.next
                fast = fast.next.next

            node = TreeNode(slow.val)
            node.left = buildDST(head, slow)
            node.right = buildDST(slow.next, tail)
            return node

        return buildDST(head, None)
