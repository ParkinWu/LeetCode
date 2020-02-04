# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
# 说明:
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        exsits = set(nums1)
        ans = set([])
        for n in nums2:
            if n in exsits:
                ans.add(n)
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]