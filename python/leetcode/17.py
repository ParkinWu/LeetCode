# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:

    def __init__(self):
        self.ds = {}
        self.ds['2'] = ['a', 'b', 'c']
        self.ds['3'] = ['d', 'e', 'f']
        self.ds['4'] = ['g', 'h', 'i']
        self.ds['5'] = ['j', 'k', 'l']
        self.ds['6'] = ['m', 'n', 'o']
        self.ds['7'] = ['p', 'q', 'r', 's']
        self.ds['8'] = ['t', 'u', 'v']
        self.ds['9'] = ['w', 'x', 'y', 'z']

    def backtracking(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.ds[digits]
        prefix = digits[:1]
        rest = digits[1:]
        res = []
        for c in self.ds[prefix]:
            cs = self.backtracking(rest)
            res.extend(map(lambda s: c + s, cs))
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        return self.backtracking(digits)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("223"))