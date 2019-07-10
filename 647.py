# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 示例 2:
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 注意:
#
# 输入的字符串长度不会超过1000。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindromic-substrings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#
#     def is_valid(self, s: str) -> bool:
#         start = 0
#         end = len(s) - 1
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True
#
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * n
#         dp[0] = 1
#         for i in range(1, n):
#             temp = 0
#             for j in reversed(range(0, i + 1)):
#                 if self.is_valid(s[j:i + 1]):
#                     temp += 1
#             dp[i] = dp[i - 1] + temp
#         return dp[-1]

class Solution:

    def countSubstrings(self, s: str) -> int:
        def countSegment(s: str, start: int, end: int) -> int:
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                print(s[start:end + 1])
                start -= 1
                end += 1
                count += 1

            return count

        ans = 0
        for i in range(len(s)):
            ans += countSegment(s, i, i)
            ans += countSegment(s, i, i + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.countSubstrings("abc"))
    print(s.countSubstrings("abcba"))
