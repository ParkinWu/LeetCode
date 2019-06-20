# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
from typing import List


class Solution:
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[-1])
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = triangle[0][0]
        for i in range(1, rows):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[rows - 1])


if __name__ == '__main__':
    s = Solution()
    m = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    print(m)
