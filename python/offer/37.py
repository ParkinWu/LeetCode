# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
# 示例: 
#
# 你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
# 注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        worklist = [root]
        ans = []
        while worklist:
            node = worklist.pop(0)
            if node:
                ans.append(str(node.val))
                worklist.append(node.left)
                worklist.append(node.right)
            else:
                ans.append('None')
        while not ans[-1]:
            ans.pop(-1)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = list(map(lambda n: int(n) if n != 'None' else None, data.split(",")))
        print(nodes)
        if not nodes[0]:
            return None
        root = TreeNode(nodes.pop(0))
        worklist = [root]
        while worklist and nodes:
            node = worklist.pop(0)
            if node and nodes:
                n = nodes.pop(0)
                left = None
                if n != None:
                    left = TreeNode(n)
                node.left = left
                worklist.append(left)

            if node and nodes:
                n = nodes.pop(0)
                right = None
                if n != None:
                    right = TreeNode(n)
                node.right = right
                worklist.append(right)

        return root


if __name__ == '__main__':
    s = Codec()
    sample = "1,2,3,None,None,4,5"
    root = s.deserialize(sample)
    assert s.serialize(root) == sample
