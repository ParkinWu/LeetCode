#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        siblings = [root]
        ans = [[root.val]]
        while True:
            tmp = []
            for node in siblings:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                break
            else:
                ans.append(list(map(lambda n: n.val, tmp)))
            siblings = tmp
        return ans

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        worklist = [[root]]
        ans = []
        while worklist:
            nodes = worklist.pop(0)
            inside = []
            for n in nodes:
                if n.left: inside.append(n.left)
                if n.right: inside.append(n.right)
            if inside:
                worklist.append(inside)
                ans.append(list(map(lambda x: x.val, inside)))
        return ans




