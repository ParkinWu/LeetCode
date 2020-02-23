# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#
#  
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：
#
# [3,9,20,15,7]
#  
#
# 提示：
#
# 节点总数 <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return []
        worklist = [root]
        while worklist:
            node = worklist.pop(0)
            ans.append(node.val)
            if node.left: worklist.append(node.left)
            if node.right: worklist.append(node.right)
        return ans
