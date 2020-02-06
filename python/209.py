# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        ans = float('inf')
        sum_of_nums = nums[0]
        while left <= right < len(nums):
            if sum_of_nums < s:
                right += 1
                if right < len(nums):
                    sum_of_nums += nums[right]
            else:
                ans = min(ans, right - left + 1)
                sum_of_nums -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans


if __name__ == '__main__':
    s = Solution()
    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3