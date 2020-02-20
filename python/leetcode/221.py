# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        maxCount = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] is '1':
                        dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
                if dp[i][j] > maxCount:
                    maxCount = dp[i][j]
        return maxCount * maxCount


if __name__ == '__main__':
    s = Solution()
    m = s.maximalSquare([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']])
    print(m)

    m = s.maximalSquare([['1', '0', '1', '0', '0']])
    print(m)

    m = s.maximalSquare([])
    print(m)

