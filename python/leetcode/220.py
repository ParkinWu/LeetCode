# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, min(i + k + 1, length)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    # assert s.containsNearbyAlmostDuplicate([2, 2], 3, 0)
    # assert s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    # assert s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
    # assert not s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
    assert not s.containsNearbyAlmostDuplicate([0, 2147483647], 1, 2147483647)