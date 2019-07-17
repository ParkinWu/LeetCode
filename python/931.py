# 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
#
# 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
#
#  
#
# 示例：
#
# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：12
# 解释：
# 可能的下降路径有：
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 和最小的下降路径是 [1,4,7]，所以答案是 12。
#
#  
#
# 提示：
#
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# class Solution:
#
#     def __init__(self):
#         self.min_total = float('inf')
#
#     def backtracking(self, A, row, l):
#         if len(A) == len(l):
#             total = 0
#             for i in l:
#                 total += A[i[0]][i[1]]
#             self.min_total = min(self.min_total, total)
#             return
#         for i in range(row, len(A)):
#             for j in range(0, len(A[0])):
#                 if len(l) > 0:
#                     (last_row, last_col) = l[-1]
#                     if i == last_row + 1 and (last_col + 1 == j or last_col == j or last_col - 1 == j):
#                         self.backtracking(A, row + 1, l + [(i, j)])
#                 elif len(l) == 0:
#                     self.backtracking(A, row + 1, l + [(i, j)])
#     # this solution will be timeout
#     def minFallingPathSum(self, A: List[List[int]]) -> int:
#         m = len(A)
#         if m == 0:
#             return 0
#         self.backtracking(A, 0, [])
#         return int(self.min_total)

class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows = len(A)
        if rows == 0:
            return 0
        cols = len(A[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dp[r][c] = A[r][c]
                elif c > 0 and c + 1 < cols:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r - 1][c + 1]) + A[r][c]
                elif c == 0:
                    dp[r][c] = min(dp[r - 1][c], dp[r - 1][c + 1]) + A[r][c]
                elif c + 1 == cols:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c]) + A[r][c]

        return int(min(dp[-1]))


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
