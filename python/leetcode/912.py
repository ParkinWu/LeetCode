# 给定一个整数数组 nums，将该数组升序排列。
#
#  
#
# 示例 1：
#
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#  
#
# 提示：
#
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:

    # def quicksort(self, nums: List[int], lo: int, hi: int) -> List[int]:
    #     if len(nums) < 2:
    #         return nums
    #     key = nums[0]
    #     left = []
    #     right = []
    #     for i in range(lo + 1, hi):
    #         if nums[i] <= key:
    #             left.append(nums[i])
    #         else:
    #             right.append(nums[i])
    #     return self.quicksort(left, 0, len(left)) + [key] + self.quicksort(right, 0, len(right))

    def partition(self, nums: List[int], lo: int, hi: int) -> int:
        k = nums[lo]
        while lo < hi:
            while lo < hi and nums[hi] >= k:
                hi -= 1
            nums[lo] = nums[hi]
            while lo < hi and nums[lo] <= k:
                lo += 1
            nums[hi] = nums[lo]
        nums[lo] = k
        return lo

    def quicksort_inplace(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return
        p = self.partition(nums, lo, hi)
        self.quicksort_inplace(nums, lo, p - 1)
        self.quicksort_inplace(nums, p + 1, hi)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort_inplace(nums, 0, len(nums) - 1)
        return nums
        # return self.quicksort(nums, 0, len(nums))

if __name__ == '__main__':
    s = Solution()
    assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]

