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
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        for i in range(1, n):
            if s[i] == ')':
                dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = 0
            if s[i] == '(':
                dp[i][0] = 0
                dp[i][1] = dp[i - 1][0]
        return max(map(lambda x: x[0], dp)) * 2


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
