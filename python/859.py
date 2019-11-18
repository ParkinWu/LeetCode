# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
#
#  
#
# 示例 1：
#
# 输入： A = "ab", B = "ba"
# 输出： true
# 示例 2：
#
# 输入： A = "ab", B = "ab"
# 输出： false
# 示例 3:
#
# 输入： A = "aa", B = "aa"
# 输出： true
# 示例 4：
#
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 示例 5：
#
# 输入： A = "", B = "aa"
# 输出： false
#  
#
# 提示：
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/buddy-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB or lenA == 0:
            return False
        diffs = []
        i = 0
        counter = set([])
        repeat = False
        while i < lenA:
            if A[i] != B[i]:
                diffs.append(i)
            if A[i] in counter:
                repeat = True
            counter.add(A[i])
            i += 1

        if len(diffs) == 0 and repeat:
            return True
        if len(diffs) != 2:
            return False
        return A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]


if __name__ == '__main__':
    s = Solution()
    assert s.buddyStrings("aa", "aa")
    assert not s.buddyStrings("ab", "ab")
    assert s.buddyStrings("ab", "ba")
    assert s.buddyStrings("aaaaaaabc", "aaaaaaacb")
    assert not s.buddyStrings("", "aa")