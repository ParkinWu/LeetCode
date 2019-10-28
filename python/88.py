# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def merge_to(self, xs1: List[int], xs2: List[int]) -> List[int]:
        if len(xs2) == 0:
            return xs1.copy()
        if len(xs1) == 0:
            return xs2.copy()
        n1 = xs1[0]
        n2 = xs2[0]
        if n2 <= n1:
            return [n2] + self.merge_to(xs1, xs2[1:])
        else:
            return [n1] + self.merge_to(xs1[1:], xs2)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = self.merge_to(nums1[:m], nums2)
        for i in range(m + n):
            nums1[i] = tmp[i]
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    # print(s.merge_to([1, 2, 3], [2, 5, 6]))
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)