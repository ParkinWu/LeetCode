# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
#
#  
#
# 示例 1：
#
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
#
# 输入："AAABBC"
# 输出：188
#  
#
# 提示：
#
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-tile-possibilities
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> List[str]:
        subs = []

        n = len(tiles)

        def subseq(start: int, s: List[str]):
            if s:
                subs.append(s)
            for i in range(start, n):
                if i > start and tiles[i] == tiles[i - 1]:
                    continue
                subseq(i + 1, s + [tiles[i]])

        ans = []

        def permute(start: int, nums: List[str], list: List[str]):
            if len(list) == len(nums) and list not in ans:
                ans.append(list.copy())
                return
            for i in range(start, n):
                permute(i + 1, nums, list + [nums[i]])

        subseq(0, [])

        for i in subs:
            permute(0, i, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numTilePossibilities("AAB"))