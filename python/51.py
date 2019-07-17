# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-queens
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def __init__(self):
        self.cols = []
        self.hill = []
        self.dale = []
        self.queens = []

    def is_under_attack(self, i: int, j: int) -> bool:
        return self.cols[j] + self.hill[i - j] + self.dale[i + j]

    def place_queen(self, i: int, j: int):
        self.cols[j] = 1
        self.hill[i - j] = 1
        self.dale[i + j] = 1
        self.queens.append((i, j))

    def remove_queen(self, i: int, j: int):
        self.cols[j] = 0
        self.hill[i - j] = 0
        self.dale[i + j] = 0
        self.queens.remove((i, j))

    def add_solution(self, res: List[str]):
        n = len(self.queens)
        result = []
        for _, col in sorted(self.queens):
            result.append('.' * col + 'Q' + '.' * (n - col - 1))
        res.append(result)

    def backtracking(self, i: int, n: int, res: List[List[str]]):
        if i == n:
            self.add_solution(res)
            return
        for i in range(i, n):
            for j in range(0, n):
                if not self.is_under_attack(i, j):
                    self.place_queen(i, j)
                    self.backtracking(i + 1, n, res)
                    self.remove_queen(i, j)
            break

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.cols = [0] * n
        self.hill = [0] * (2 * n - 1)
        self.dale = [0] * (2 * n - 1)
        self.backtracking(0, n, res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(5))
