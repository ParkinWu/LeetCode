# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def backtracking(self, res: List[str], cur: str, open: int, close: int, max: int):
        if len(cur) == max * 2:
            res.append(cur)
            return

        if open < max:
            self.backtracking(res, cur + '(', open + 1, close, max)
        if close < open:
            self.backtracking(res, cur + ')', open, close + 1, max)


    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        self.backtracking(s, "", 0, 0, n)
        return s

if __name__ == '__main__':
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)