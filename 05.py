# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = ""
        for j in range(n):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome(""))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
