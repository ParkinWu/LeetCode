# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-partitioning
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        length = len(s)
        start = 0
        end = length - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def backtracking(self, s: str, start: int, list: List[str], ans: List[List[str]]):
        if start == len(s):
            ans.append(list.copy())
            return

        for i in range(start, len(s)):
            if self.is_palindrome(s[start:i + 1]):
                list.append(s[start:i + 1])
                self.backtracking(s, i + 1, list, ans)
                list.pop(-1)

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtracking(s, 0, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))