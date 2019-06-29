# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:

    def __init__(self):
        self.ans = []

    def backtracking(self, candidates: List[int], target: int, sum: int, list: List[int]):
        if target == sum:
            copy = list.copy()
            copy.sort()
            if copy not in self.ans:
                self.ans.append(copy)
                return
        if target < sum:
            return
        for n in candidates:
            list.append(n)
            self.backtracking(candidates, target, sum + n, list)
            list.pop(-1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0, [])
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
