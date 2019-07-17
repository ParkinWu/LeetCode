# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
#
# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
#
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
#
# 示例:
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
# 注意:
#
# N 的取值范围是 [1, 10000]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotated-digits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(N + 1):
            isGoodNumber = False
            rest = i
            while rest > 0:
                bit = rest % 10
                if bit == 3 or bit == 4 or bit == 7:
                    break
                isGoodNumber |= bit == 2 or bit == 5 or bit == 6 or bit == 9
                rest = rest // 10
            if isGoodNumber and rest == 0:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    assert s.rotatedDigits(857) == 247