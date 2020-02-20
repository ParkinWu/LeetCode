# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-rectangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    # timeout
    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #     area = 0
    #     rows = len(matrix)
    #     cols = len(matrix[0]) if rows else 0
    #     dp = [[0] * cols for _ in range(rows)]
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == '0':
    #                 continue
    #             dp[i][j] = dp[i][j - 1] + 1 if j else 1
    #             width = dp[i][j]
    #             for k in range(i, -1, -1):
    #                 width = min(width, dp[k][j])
    #                 area = max(area, width * (i - k + 1))
    #     return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = dp[i][j - 1] + 1 if j else 1
                width = dp[i][j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    area = max(area, width * (i - k + 1))
        return area


if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))



