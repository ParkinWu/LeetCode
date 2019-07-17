# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#  
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
#
# 说明:
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        return False


def build_tree(l: List[int]) -> TreeNode:
    l = [0] + l
    i = 1
    ans = None

    nodes = list(map(lambda val: TreeNode(val) if val != None else None, l))

    while 2 * i < len(nodes):
        node = nodes[i]
        if i == 1:
            ans = node
        left = nodes[2 * i]
        right = nodes[2 * i + 1]
        node.left = left
        node.right = right
        i += 1
    return ans


def print_tree(root: TreeNode) -> str:
    s = " "
    if not root:
        return " "
    queue = [root]
    while queue:
        for n in queue:
            if n == None:
                s += "N"
            else:
                s += str(n)
            s += " "
        new_queue = []
        for n in queue:
            if not n:
                continue
            new_queue.append(n.left)
            new_queue.append(n.right)
            s += "  "
        queue = new_queue
        s += "\n"
    return s


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return right if not left else left if not right else root


if __name__ == '__main__':
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(print_tree(root))
    s = Solution()
    print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(0)))


