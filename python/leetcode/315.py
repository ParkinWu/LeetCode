# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
# 示例:
#
# 输入: [5,2,6,1]
# 输出: [2,1,1,0]
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 0


class Solution:

    def insertNode(self, root: TreeNode, val, res, res_idx) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, val, res, res_idx)
        elif val > root.val:
            res[res_idx] += root.count + 1
            root.right = self.insertNode(root.right, val, res, res_idx)
        return root

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        root = None
        ans = [0 for _ in range(n)]
        for i in reversed(range(n)):
            root = self.insertNode(root, nums[i], ans, i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))
    print(s.countSmaller([]))
    print(s.countSmaller([5]))
    print(s.countSmaller([-1, 5]))
    print(s.countSmaller([2, 0, 1]))
