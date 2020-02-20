# 假定 BST 有如下定义：
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
# 返回[2].
#
# 提示：如果众数超过1个，不需考虑输出顺序
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        occurs = {}

        def travel(r: TreeNode):
            if not r:
                return
            occurs[r.val] = occurs.get(r.val, 0) + 1
            travel(r.left)
            travel(r.right)
        if not root:
            return []
        travel(root)
        ans = []
        max_times = max(occurs.values())
        for k, v in occurs.items():
            if v == max_times:
                ans.append(k)
        return ans



