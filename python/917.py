# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#  
#
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
# 示例 2：
#
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：
#
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
#
# 提示：
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-only-letters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0
        right = len(S) - 1
        ans = list(S)
        while left < right:
            while left < right and not S[left].isalpha():
                left += 1
            while left < right and not S[right].isalpha():
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = S[right], S[left]
            left += 1
            right -= 1
        return "".join(ans)


if __name__ == '__main__':
    s = Solution()
    assert s.reverseOnlyLetters("7_28]") == "7_28]"
    assert s.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert s.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert s.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
