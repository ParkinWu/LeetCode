# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
#
# 示例:
#
# s = "abaccdeff"
# 返回 "b"
#
# s = ""
# 返回 " "
#  
#
# 限制：
#
# 0 <= s 的长度 <= 50000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def firstUniqChar(self, s: str) -> str:
        # recored count of character
        occurs = {}
        # recored a character where it first appeared
        indexs = {}
        ans = " "
        idx = float('inf')
        for (i, c) in enumerate(s):
            if c not in indexs:
                indexs[c] = i
            occurs[c] = occurs.get(c, 0) + 1

        for k in occurs:
            if occurs[k] == 1 and indexs[k] < idx:
                ans = k
                idx = indexs[k]
        return ans