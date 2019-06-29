# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def backtracking(self, nums: List[int], list: List[int]):
        if not nums:
            copy = list.copy()
            if copy not in self.ans:
                self.ans.append(copy)
        for n in nums:
            list.append(n)
            copy = nums.copy()
            copy.remove(n)
            self.backtracking(copy, list)
            list.pop(-1)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, [])
        return self.ans


if __name__ == '__main__':
    s =  Solution()
    print(s.permuteUnique([1, 1, 2]))
