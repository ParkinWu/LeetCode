# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#  
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#  
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
#
# 限制：
#
# 1 <= s 的长度 <= 8
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List, Set
class Solution:
    def backtracking(self, s: str, flags: List[int], res: str, ans: Set[str]):
        if len(s) == len(res):
            ans.add(res)
            return
        for i in range(len(s)):
            if flags[i] == 1: continue
            flags[i] = 1
            self.backtracking(s, flags, res + s[i], ans)
            flags[i] = 0

    def permutation(self, s: str) -> List[str]:
        flags = [0] * len(s)
        ans = set([])
        self.backtracking(s, flags, "", ans)
        return list(ans)


