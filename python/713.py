# 给定一个正整数数组 nums。
#
# 找出该数组内乘积小于 k 的连续的子数组的个数。
#
# 示例 1:
#
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
# 说明:
#
# 0 < nums.length <= 50000
# 0 < nums[i] < 1000
# 0 <= k < 10^6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from functools import reduce
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        acc = 1
        ans = 0
        for right, v in enumerate(nums):
            acc *= v
            while acc >= k:
                acc /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # assert s.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert s.numSubarrayProductLessThanK([1, 2, 3], 0) == 0




