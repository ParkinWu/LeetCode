# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class MaxHeap:
    def __init__(self, cap):
        self.pq = [float('-inf')] * (cap + 1)
        self.root = None
        self.count = 0

    def __swap(self, i: int, j: int):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def __swim(self, i: int):
        while i > 1 and self.pq[i // 2] < self.pq[i]:
            self.__swap(i, i // 2)
            i = i // 2

    def __sink(self, i: int):
        while 2 * i <= self.count:
            j = 2 * i
            if j < self.count and self.pq[j] < self.pq[j + 1]:
                j += 1
            if self.pq[i] >= self.pq[j]:
                break
            self.__swap(j, i)
            i = j

    def insert(self, val: int):
        self.count += 1
        self.pq[self.count] = val
        self.__swim(self.count)

    def pop_max(self) -> int:
        max = self.pq[1]
        self.__swap(1, self.count)
        self.count -= 1
        self.pq[self.count + 1] = float('-inf')
        self.__sink(1)
        return max


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(len(nums))
        for n in nums:
            heap.insert(n)

        ans = 0
        for i in range(k):
            ans = heap.pop_max()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 1))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 3))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 4))