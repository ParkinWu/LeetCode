# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
#
#  
#
# 示例:
#
# 输入: a = 1, b = 1
# 输出: 2
#  
#
# 提示：
#
# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def add(self, a: int, b: int) -> int:
        while a != 0:
            tmp = a ^ b
            a = (a & b) << 1
            b = tmp
        return b


if __name__ == '__main__':
    s = Solution()
    assert s.add(-1, 2) == 1
    assert s.add(1, 1) == 2
    assert s.add(0, 1) == 1
    assert s.add(0, 0) == 0
    assert s.add(9, 1) == 10