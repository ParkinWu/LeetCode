# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    # DP easily to understand but timeout
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n <= 1:
    #         return 0
    #     dp = [float('inf')] * n
    #     dp[0] = 0
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] >= i - j:
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #     return int(dp[n - 1])

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [0] * n
        dp[0] = 0
        for i in range(n):
            for j in reversed(range(1, nums[i] + 1)):
                if i + j >= n - 1:
                    return dp[i] + 1
                elif dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1
                else:
                    break
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
