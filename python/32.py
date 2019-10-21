# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.longestValidParentheses("(()"))
    # print(s.longestValidParentheses(")()())"))
    # print(s.longestValidParentheses(")("))
    print(s.longestValidParentheses("()"))
