# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#
# 若这两个字符串没有公共子序列，则返回 0。
#
#  
#
# 示例 1:
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 示例 2:
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
# 示例 3:
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
#  
#
# 提示:
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i - 1][j - 1] + 1) if i > 0 and j > 0 else 1
                else:
                    dp[i][j] = max(dp[i - 1][j] if i > 0 else 0, dp[i][j - 1] if j > 0 else 0)

        return max(dp[-1])


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    assert s.longestCommonSubsequence("abcef", "adef") == 3