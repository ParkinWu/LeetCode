# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
#
# 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
#
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
#
# 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
#
#  
#
# 示例 1：
#
# 输入: piles = [3,6,7,11], H = 8
# 输出: 4
# 示例 2：
#
# 输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
# 示例 3：
#
# 输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
#  
#
# 提示：
#
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/koko-eating-bananas
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import math
class Solution:
    def calculate_hours(self, piles: List[int], k: int) -> int:
        acc = 0
        for n in piles:
            acc += (math.ceil(n / k))
        return acc

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        while left < right:
            mid = (left + right) // 2
            hours = self.calculate_hours(piles, mid)
            if hours <= H:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    assert s.minEatingSpeed([312884470], 968709470) == 1
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert s.minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
, 823855818) == 14