# 累加数是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
#
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 示例 1:
#
# 输入: "112358"
# 输出: true
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2:
#
# 输入: "199100199"
# 输出: true
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/additive-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def is_vaild(self, s: str, list: List[int]) -> bool:
        n = len(s)
        if n == 0:
            return False
        if n > 1 and s[0] == '0':
            return False
        if len(list) < 2:
            return True
        return int(s) == list[-1] + list[-2]

    def backtracking(self, num: str, start: int, list: List[int], ans: List[List[int]]):
        if start == len(num) and len(list) > 2:
            ans.append(list.copy())
            return
        for i in range(1, len(num) - start + 1):
            s = num[start:start+i]
            if not self.is_vaild(s, list):
                continue
            self.backtracking(num, start + i, list + [int(s)], ans)

    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        if len(num) < 3:
            return False

        self.backtracking(num, 0, [], ans)
        print(ans)
        return len(ans) > 0


if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))
