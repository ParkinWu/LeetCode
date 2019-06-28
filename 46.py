# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        res = []
        for i in range(len(nums)):
            copy = nums.copy()
            one = copy.pop(i)
            res += list(map(lambda l: [one] + l, self.permute(copy)))
        return res


if __name__ == '__main__':
    s = Solution()
    l = s.permute([1, 2, 3])
    print(l)