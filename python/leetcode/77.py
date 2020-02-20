# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combinations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def select(self, nums: List[int], n: int) -> List[List[int]]:
        if n == 0 or len(nums) < n:
            return [[]]
        if n == len(nums):
            return [nums]
        one = nums[:1]
        rest = self.select(nums[1:], n - 1)
        return list(map(lambda x: one + x, rest)) + self.select(nums[1:], n)

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        return self.select(nums, k)


if __name__ == '__main__':
    s = Solution()
    r = s.combine(1, 1)
    print(r)

