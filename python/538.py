# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
# 例如：
#
# 输入: 二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def search(self, root: TreeNode, val: int) -> int:
        if not root:
            return val
        root.val += self.search(root.right, val)
        return self.search(root.left, root.val)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.search(root, 0)
        return root




