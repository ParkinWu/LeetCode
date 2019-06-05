# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

class Solution:

    def __init__(self):
        self.cache = {}
    # 总方法数 = 本次走1阶的方法数 + 本次走2台阶的方法数
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        cache = self.cache.get(n)
        if cache:
            return cache
        stairs = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = stairs
        return stairs


if __name__ == '__main__':
    s = Solution()
    n = s.climbStairs(3)
    print(n)

    s = Solution()
    n = s.climbStairs(35)
    print(n)
