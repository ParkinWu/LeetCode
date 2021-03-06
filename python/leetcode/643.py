# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#  
#
# 注意:
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    # Solution 1
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     n = len(nums)
    #     dp = [0] * n
    #     sum = 0
    #     for i in range(n):
    #         sum += nums[i]
    #         dp[i] = sum
    #
    #     aver = dp[k - 1] / k
    #     for i in range(k, n):
    #         aver = max(aver, (dp[i] - dp[i - k]) / k)
    #     return aver

    # Solution 2
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = 0
        for i in range(k):
            sum += nums[i]

        ans = sum
        for i in range(k, n):
            sum = sum - nums[i - k] + nums[i]
            ans = max(ans, sum)

        return ans / k


if __name__ == '__main__':
    s = Solution()
    # assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
    # assert s.findMaxAverage([0, 1, 1, 3, 3], 4) == 2
    assert s.findMaxAverage([4, 2, 1, 3, 3], 2) == 3


