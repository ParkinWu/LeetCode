# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
#  
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  
#
# 提示：
#
# 0 <= num < 231
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List, Set
class Solution:
    def backtracking(self, chars: [str], s: str, res: str, ans: Set[str]):
        if not s:
            ans.add(res)
            return
        if s[:1] and 0 <= int(s[:1]) <= 25:
            self.backtracking(chars, s[1:], res + chars[int(s[:1])], ans)
        if s[:2] and 0 <= int(s[:2]) <= 25 and s[:1] != "0":
            self.backtracking(chars, s[2:], res + chars[int(s[:2])], ans)

    def translateNum(self, num: int) -> int:
        s = str(num)
        ans = set([])
        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        self.backtracking(chars, s, "", ans)
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    assert s.translateNum(506) == 1
    assert s.translateNum(12258) == 5