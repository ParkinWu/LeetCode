# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
#
# 示例 1:
#
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "xtfn"。
# 示例 2:
#
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。
# 示例 3:
#
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def bits(self, s: str) -> int:
        res = 0
        for c in s:
            res |= 1 << (ord(c) - ord('a'))
        return res

    def maxProduct(self, words: List[str]) -> int:
        bitsmap = {}
        for s in words:
            bitsmap[s] = self.bits(s)

        maxProduct = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitsmap[words[i]] & bitsmap[words[j]] == 0:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct
