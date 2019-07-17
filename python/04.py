from typing import List
import math


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        # 如果是总数是奇数个，则左侧是mid个，右侧是mid + 1个
        # 如果总数是偶数个，则左侧和右侧都是mid个
        mid = total // 2

        # 保证最短的数组在上面
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        # 第一个数组，中间分隔
        leftIndex1 = math.ceil(len1 / 2)
        leftIndex2 = mid - leftIndex1
        while True:
            left1 = nums1[:leftIndex1]
            right1 = nums1[leftIndex1:]

            left2 = nums2[:leftIndex2]
            right2 = nums2[leftIndex2:]

            l1 = float("-inf")
            if len(left1) > 0:
                l1 = left1[-1]
            l2 = float("-inf")
            if len(left2) > 0:
                l2 = left2[-1]

            r1 = float("inf")
            if len(right1) > 0:
                r1 = right1[0]
            r2 = float("inf")
            if len(right2) > 0:
                r2 = right2[0]

            maxLeft = max(l1, l2)
            minRight = min(r1, r2)

            if maxLeft <= minRight:
                if total % 2 == 1:
                    return minRight
                else:
                    return (minRight + maxLeft) / 2
            else:
                if l1 > l2:
                    new = math.ceil(leftIndex1 / 2)
                    if leftIndex1 == new:
                        new = new - 1
                    leftIndex1 = new
                    leftIndex2 = mid - leftIndex1
                else:
                    leftIndex1 = leftIndex1 + math.ceil(len(right1) / 2)
                    leftIndex2 = mid - leftIndex1



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2,6,7,8], [3, 4, 5, 9, 10]))
    print(s.findMedianSortedArrays([1], [1]))
    print(s.findMedianSortedArrays([1], [2, 3, 4, 5, 6]))
    print(s.findMedianSortedArrays([1], [2, 3]))
    print(s.findMedianSortedArrays([], [1]))
    print(s.findMedianSortedArrays([2], [1]))
    print(s.findMedianSortedArrays([1], [2, 3]))
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([], [1,2, 3, 4, 5]))
