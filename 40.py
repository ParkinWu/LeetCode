# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def backtracking(self, candidates: List[int], target: int, begin: int, sum: int, list: List[int]):
        if sum == target and list not in self.ans:
            self.ans.append(list.copy())
            return
        if sum > target:
            return

        for i in range(begin, len(candidates)):
            list.append(candidates[i])
            self.backtracking(candidates, target, i + 1, sum + candidates[i], list)
            list.pop(-1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [])
        return self.ans


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum2([10,1,2,7,6,1,5], 8)
    print(res)
