# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret, up, down = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            if n >= 0:
                up, down = max(up * n, n), min(down * n, n)
            else:
                up, down = max(down * n, n), min(up * n, n)
            ret = max(ret, up)
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([0, 2]) == 2
    assert s.maxProduct([-2, 3, -4]) == 24