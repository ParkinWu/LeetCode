# 统计一个数字在排序数组中出现的次数。
#
#  
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#  
#
# 限制：
#
# 0 <= 数组长度 <= 50000
#
#  
#
# 注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)