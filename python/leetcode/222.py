# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # solution 1: 直接递归, 但是没用到题目给到的完全二叉树的前提
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # solution 2: 利用性质：完全二叉树最左叶子节点就是整个树的最大高度
    def countNodes(self, root: TreeNode) -> int:

        # 计算二叉树的最大高度, 利用性质：完全二叉树最左叶子节点就是整个树的最大高度
        def max_deep(r: TreeNode) -> int:
            if not r:
                return 0
            ans = 1
            while r.left:
                ans += 1
                r = r.left
            return ans

        if not root:
            return 0
        # 不含根节点
        max_deep_l = max_deep(root.left)
        max_deep_r = max_deep(root.right)
        # 相等，说明左子树是满的
        if max_deep_l == max_deep_r:
            return 1 + 2 ** max_deep_l - 1 + self.countNodes(root.right)
        # 左边大，说明右子树是满的
        if max_deep_l > max_deep_r:
            return 1 + 2 ** max_deep_r - 1 + self.countNodes(root.left)
        # 不会走到这里，完全二叉树的左子树高度 >= 右子树高度
        return 1



