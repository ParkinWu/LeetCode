# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 回溯法，时间复杂度不满足要求
# class Solution:
#     def backtracking(self, nums: List[int], start: int, list: List[int], ans: List[List[int]]):
#         if len(list) == 3 and sum(list) == 0 and list not in ans:
#             ans.append(list.copy())
#             return
#         for i in range(start, len(nums)):
#             n = nums[start]
#             self.backtracking(nums, i + 1, list + [n], ans)
#
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         nums.sort()
#         for i in range(0, len(nums)):
#             self.backtracking(nums, i, [], ans)
#         return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums)):
            self.backtracking(nums, i, [], ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0,4,-1,0,3,1,1,0,-3,2,-5,-4,-3,0,0,-3]))
