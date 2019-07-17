# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def backtracking(self, k: int, n: int, begin: int, sum: int, list: List[int]):
        if k == 0 and sum == n:
            self.ans.append(list.copy())
            return
        for i in range(begin, 10):
            list.append(i)
            self.backtracking(k - 1, n, i + 1, sum + i, list)
            list.pop(-1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1, 0, [])
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))