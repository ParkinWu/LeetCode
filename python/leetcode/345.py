# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        left = 0
        right = n - 1
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        cs = list(s)
        while left < right:
            while left <= n - 1 and cs[left] not in vowel:
                left += 1
            while right >= 0 and cs[right] not in vowel:
                right -= 1
            if left < right:
                cs[left], cs[right] = cs[right], cs[left]
                left += 1
                right -= 1

        return "".join(cs)


if __name__ == '__main__':
    s = Solution()
    # assert s.reverseVowels("hello") == "holle"
    # assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels(".,") == ".,"
