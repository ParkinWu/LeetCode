# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#  
#
# 示例 1：
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
#
# 限制：
#
# 0 <= 节点个数 <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isEq(self, r1: TreeNode, r2: TreeNode) -> bool:
        if not r1 and not r2:
            return True
        if not (r1 and r2) or r1.val != r2.val:
            return False
        return self.isEq(r1.left, r2.left) and self.isEq(r1.right, r2.right)

    def symmetric(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.symmetric(root.left)
        right = self.symmetric(root.right)
        root.left, root.right = right, left
        return root

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        mirrorRight = self.symmetric(root.right)
        # print(mirrorRight)
        # print(root.left)
        return self.isEq(root.left, mirrorRight)