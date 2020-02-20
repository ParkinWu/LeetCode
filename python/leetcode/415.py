# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        cs1 = list(num1)
        cs2 = list(num2)
        stack = []
        bits = []
        while cs1 or cs2:
            c1 = 0
            c2 = 0
            if cs1:
                c1 = cs1.pop(-1)
            if cs2:
                c2 = cs2.pop(-1)

            stack.append(int(c1))
            stack.append(int(c2))
            s = sum(stack)
            rest = s % 10
            carry = s // 10
            bits.insert(0, str(rest))
            stack = [carry]
        if stack[0] > 0:
            bits.insert(0, str(stack[0]))

        return "".join(bits)


if __name__ == '__main__':
    s = Solution()
    # assert s.addStrings("123", "129") == "252"
    assert s.addStrings("123", "929") == "1052"

