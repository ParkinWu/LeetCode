# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
#
# 示例2:
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#  
#
# 注意：
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutation-in-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        s1map = {}
        s2map = {}
        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1

        for i in range(len1):
            c = s2[i]
            s2map[c] = s2map.get(c, 0) + 1

        if s1map == s2map:
            return True
        for i in range(len1, len2):
            remove = s2[i - len1]
            add = s2[i]
            if s2map[remove] > 1:
                s2map[remove] -= 1
            else:
                s2map.pop(remove)
            s2map[add] = s2map.get(add, 0) + 1
            if s1map == s2map:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    # assert s.checkInclusion("ab", "eidbaooo")
    # assert not s.checkInclusion("ab", "eidboaoo")
    assert not s.checkInclusion("ab", "a")



