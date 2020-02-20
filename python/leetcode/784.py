# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
# 注意：
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-case-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def reverseChar(self, c: str) -> str:
        if 'A' <= c <= 'Z':
            c = chr(ord(c) + 32)
        elif 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        return c

    def letterCasePermutation(self, S: str) -> List[str]:

        if not S:
            return [""]
        c = S[:1]
        rest = self.letterCasePermutation(S[1:])
        if c == self.reverseChar(c):
            return list(map(lambda x: c + x, rest))

        return list(map(lambda x: self.reverseChar(c) + x, rest)) + list(map(lambda x: c + x, rest))


if __name__ == '__main__':
    s = Solution()
    res = s.letterCasePermutation("C")
    print(res)



