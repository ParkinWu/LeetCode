# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import  List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def backtracking(start: int, list: List[int]):
            ans.append(list)
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtracking(i + 1, list + [nums[i]])

        backtracking(0, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,3,4,5,6,7,8,10,0]))