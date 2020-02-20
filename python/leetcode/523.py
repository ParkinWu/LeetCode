# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
#
# 示例 1:
#
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
# 示例 2:
#
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
# 说明:
#
# 数组的长度不会超过10,000。
# 你可以认为所有数字总和在 32 位有符号整数范围内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/continuous-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        acc = 0
        s = set([])
        cache = 0
        for i in range(len(nums)):
            acc += nums[i]
            res = acc if k == 0 else acc % k
            if res in s:
                return True
            s.add(cache)
            cache = res
        return False







if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(s.checkSubarraySum([23, 2, 6, 4, 7], 0))
    print(s.checkSubarraySum([23, 2, 6, 4, 7], -6))
    print(s.checkSubarraySum([0, 1, 0], -1))
    print(s.checkSubarraySum([0], 0))
    print(s.checkSubarraySum([0, 0], 0))
    print(s.checkSubarraySum([1, 2, 3], 6))
    print(s.checkSubarraySum([23, 2, 6, 4, 7], 0))

