# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

from typing import List

class Solution:
    # 递推公式 F(i, j) = min(F(i - 1, j) , F(i, j - 1)) + grid[i][j]
    # 边界条件：当处于第一行或者第一列的时候，只有一个选项
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        flags = [[float('inf')] * cols for _ in range(rows)]
        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 and j == 0:
                    flags[i][j] = grid[i][j]
                elif i == 0:
                    flags[i][j] = flags[i][j - 1] + grid[i][j]
                elif j == 0:
                    flags[i][j] = flags[i - 1][j] + grid[i][j]
                else:
                    flags[i][j] = min(flags[i - 1][j], flags[i][j - 1]) + grid[i][j]
        return flags[rows - 1][cols - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print(r)