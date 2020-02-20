# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surrounded-regions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class FindUnion:
    def __init__(self):
        pass

    def find(self, x: int):
        pass

    def union(self, x: int, y: int):
        pass

    def is_connection(self, x: int, y: int) -> bool:
        pass


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_rows = len(board)
        if n_rows == 0:
            return
        n_cols = len(board[0])
        # 1. we replace the 'O' by 'B' on the boundary

        # the first row and the last row
        for i in range(n_cols):
            if board[0][i] == "O":
                board[0][i] = "B"
            if board[n_rows - 1][i] == "O":
                board[n_rows - 1][i] = "B"
        # the first column and the last column
        for i in range(n_rows):
            if board[i][0] == "O":
                board[i][0] = "B"
            if board[i][n_cols - 1] == "O":
                board[i][n_cols - 1] = "B"
        # 2. enumerate all the positions in the board

        fu = FindUnion()
        for r in range(n_rows):
            for c in  range(n_cols):
                if board[r][c] == "O":
                    if r - 1 >= 0 and board[r - 1][c] == "B":
                        




