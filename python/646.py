# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
#
# 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
#
# 给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
#
# 示例 :
#
# 输入: [[1,2], [2,3], [3,4]]
# 输出: 2
# 解释: 最长的数对链是 [1,2] -> [3,4]
# 注意：
#
# 给出数对的个数在 [1, 1000] 范围内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        if n < 2:
            return 0
        dp = [1] * n
        for i in range(0, n):
            l = [pairs[i]]
            head = pairs[i]
            for j in range(n):
                if head[0] <= pairs[j][1]:
                    continue
                head = pairs[j]
                l.insert(0, pairs[j])
                dp[i] = max(dp[j] + 1, dp[i])
            print(l)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestChain([[9, 10], [9, 10], [4, 5], [-9, -3], [-9, 1], [0, 3], [6, 10], [-5, -4], [-7, -6]]))
    print(s.findLongestChain([[-1, 1], [-2, 7], [-5, 8], [-3, 8], [1, 3], [-2, 9], [-5, 2]]))
    print(s.findLongestChain([[3, 4], [2, 3], [1, 2]]))
    print(s.findLongestChain([[1, 2], [2, 3]]))
    print(s.findLongestChain([[1, 2], [2, 3], [3, 4]]))
    print(s.findLongestChain([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [8, 9]]))