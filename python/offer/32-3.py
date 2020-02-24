# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
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
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#
# 提示：
#
# 节点总数 <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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
        worklist = [[root]]
        ans = [[root.val]]
        should_reverse = True
        while worklist:
            queue = worklist.pop(0)
            new_queue = []
            for n in queue:
                if n.left: new_queue.append(n.left)
                if n.right: new_queue.append(n.right)
            if new_queue: worklist.append(new_queue)
            inner = []

            for n in new_queue:
                insertAt = 0 if should_reverse else len(new_queue)
                inner.insert(insertAt, n.val)
            should_reverse = not should_reverse
            if inner: ans.append(inner)

        return ans

