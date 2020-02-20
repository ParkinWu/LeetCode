# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-squares
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# from math import sqrt
#
# class Solution:
#     def __init__(self):
#         self.cache = {}
#
#     def numSquares(self, n: int) -> int:
#         if n <= 3:
#             return n
#         if n in self.cache:
#             return self.cache[n]
#
#         count = float('inf')
#         for i in reversed(range(1, int(sqrt(n)) + 1)):
#             if i * i <= n:
#                 count = min(1 + self.numSquares(n - i * i), count)
#         self.cache[n] = count
#         return count

# 四平方数和定理
class Solution:
    def numSquares(self, n) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(7168))

