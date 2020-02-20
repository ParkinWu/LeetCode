# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 找到规律:
# 假设 S0S1S2...Sn为输入字符串
# 字符串解码总个数 = 首字母单独解码总个数 + 前两个字符单独解码的总个数
# numDecode(Si -> Sn) = numDecode(Si+1 -> Sn) + (numDecode(Si+2 -> Sn) if Int(SiSi+1) ∈ [1, 26] else 0)

class Solution:
    def is_accept(self, s: str) -> bool:
        if not s:
            return True
        n = int(s)
        return 1 <= n <= 26

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 2)
        dp[n] = 1 if self.is_accept(s[n:]) else 0
        dp[n - 1] = 1 if self.is_accept(s[n-1:]) else 0
        for i in reversed(range(0, n - 1)):
            if s[i:i+1] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] + (dp[i + 2] if self.is_accept(s[i:i+2]) else 0)
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings("01") == 0
    assert s.numDecodings("0") == 0
    assert s.numDecodings("1") == 1
    assert s.numDecodings("10") == 1
    assert s.numDecodings("12") == 2
    assert s.numDecodings("27") == 1
    assert s.numDecodings("226") == 3

