# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/top-k-frequent-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class MaxHeap:
    def __init__(self, cap):
        self.pq = [(float('-inf'), 0)] * (cap + 1)
        self.count = 0

    def __swim(self, i: int):
        while i > 1 and self.pq[i][1] > self.pq[i // 2][1]:
            self.__swap(i, i // 2)
            i = i // 2

    def __sink(self, i: int):
        while 2 * i < self.count:
            j = 2 * i
            if j < self.count and self.pq[j][1] < self.pq[j + 1][1]:
                j += 1
            if self.pq[j][1] <= self.pq[i][1]:
                break
            self.__swap(i, j)
            i = j

    def __swap(self, i: int, j: int):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def insert(self, kv):
        self.count += 1
        self.pq[self.count] = kv
        self.__swim(self.count)

    def pop_max(self):
        max = self.pq[1]
        self.__swap(1, self.count)
        self.count -= 1
        self.pq[self.count + 1] = (float('-inf'), 0)
        self.__sink(1)
        return max

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequecies = {}
        for n in nums:
            if frequecies.get(n):
                frequecies[n] = frequecies[n] + 1
            else:
                frequecies[n] = 1

        heap = MaxHeap(len(frequecies))
        for key, val in frequecies.items():
            heap.insert((key, val))
        ans = []
        for i in range(k):
            max = heap.pop_max()
            ans.append(max[0])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 10))
    # print(s.topKFrequent([1], 1))