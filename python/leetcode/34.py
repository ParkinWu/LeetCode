# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:

    def bisect_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def bisect_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums or target < nums[0] or target > nums[-1]:
            return ans

        insert_before = self.bisect_left(nums, target)
        insert_after = self.bisect_right(nums, target)

        if insert_after - 1 >= 0 and nums[insert_after - 1] == target:
            ans[1] = insert_after - 1
        if insert_before >= 0 and nums[insert_before] == target:
            ans[0] = insert_before
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.searchRange([2, 2], 3) == [-1, -1]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 1) == [-1, -1]