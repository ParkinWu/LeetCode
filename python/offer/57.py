# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
# 示例 2：
#
# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
#  
#
# 限制：
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:

    def findN(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left < len(nums) and nums[left] == target

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = nums[i]
            if n < target and self.findN(nums, target - n):
                return [n, target - n]
        return []