# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
#
# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
#
# 例 1：
#
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
# 3	6	9
#
# 第5小的数字是 3 (1, 2, 2, 3, 3).
# 例 2：
#
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
#
# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).
# 注意：
#
# m 和 n 的范围在 [1, 30000] 之间。
# k 的范围在 [1, m * n] 之间。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def search_less_or_eq(self, m: int, n: int, target: int) -> int:
        i = m
        j = 1
        ans = 0
        while j <= n and i >= 1:
            if i * j <= target:
                ans += i
                j += 1
            else:
                i -= 1
        return ans

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        while left < right:
            mid = (left + right) // 2
            cnt = self.search_less_or_eq(m, n, mid)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    assert s.search_less_or_eq(3, 3, 0) == 0
    assert s.search_less_or_eq(3, 3, 1) == 1
    assert s.search_less_or_eq(3, 3, 2) == 3

    assert s.findKthNumber(3, 3, 5) == 3
    assert s.findKthNumber(2, 3, 6) == 6

