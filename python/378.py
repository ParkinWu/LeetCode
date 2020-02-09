# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
# 说明:
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def lessOrEqCount(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        i = rows - 1
        j = 0
        ans = 0
        while i >= 0 and j < cols:
            if matrix[i][j] <= target:
                ans += (i + 1)
                j += 1
            else:
                i -= 1
        return ans

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            cnt = self.lessOrEqCount(matrix, mid)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    assert s.lessOrEqCount([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 0) == 0
    assert s.lessOrEqCount([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 1) == 1
    assert s.lessOrEqCount([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 5) == 2
    assert s.lessOrEqCount([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 10) == 4
    assert s.lessOrEqCount([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 13) == 8

    assert s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13