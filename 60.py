# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# #
# # 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# #
# # "123"
# # "132"
# # "213"
# # "231"
# # "312"
# # "321"
# # 给定 n 和 k，返回第 k 个排列。
# #
# # 说明：
# #
# # 给定 n 的范围是 [1, 9]。
# # 给定 k 的范围是[1,  n!]。
# # 示例 1:
# #
# # 输入: n = 3, k = 3
# # 输出: "213"
# # 示例 2:
# #
# # 输入: n = 4, k = 9
# # 输出: "2314"
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/permutation-sequence
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def __init__(self):
        self.cache = [0] * 9

    def fact(self, n: int) -> int:
        if n == 1:
            return 1
        if self.cache[n] > 0:
            return self.cache[n]
        self.cache[n] = n * self.fact(n - 1)
        return self.cache[n]

    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        nums = [i for i in range(1, n + 1)]
        if n == 1:
            return "1"
        # 从左到右，第1个bit，相同的个数有 fact(n - 1)个
        while k > 1:
            # 计算有多少种选择
            choices = self.fact(n - 1)
            # 计算选择的位置
            i = (k - 1) // choices
            # 把当前字符加上
            ans += str(nums.pop(i))
            # 计算下一位
            k = (k - 1) % choices + 1
            n = len(nums)

        for n in nums:
            ans += str(n)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 2))
    print(s.getPermutation(2, 2))
    print(s.getPermutation(3, 3))
    print(s.getPermutation(4, 9))

