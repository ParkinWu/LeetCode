# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#  
#
# 示例 1:
#
# 输入: 1
# 输出: "1"
# 示例 2:
#
# 输入: 4
# 输出: "1211"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-and-say
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def nextWord(self, word: str) -> str:
        s = ""
        current = word[0]
        count = 0
        for c in word:
            if current == c:
                count += 1
            else:
                s += (str(count) + current)
                current = c
                count = 1
        if count > 0:
            s += (str(count) + current)
        return s

    def countAndSay(self, n: int) -> str:
        word = "1"
        for _ in range(1, n):
            word = self.nextWord(word)
        return word


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(30))
    # assert s.nextWord("1") == "11"
    # assert s.nextWord("11") == "21"
    # assert s.nextWord("21") == "1211"
    # assert s.nextWord("1211") == "111221"