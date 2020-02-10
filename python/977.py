# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#  
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
#
# 提示：
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        ans = []
        while left <= right:
            sqrt_left = A[left] * A[left]
            sqrt_right = A[right] * A[right]
            if sqrt_left >= sqrt_right:
                ans.insert(0, sqrt_left)
                left += 1
            else:
                ans.insert(0, sqrt_right)
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]