# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#  
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#  
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#  
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    # timeout
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     n = len(heights)
    #     for i in range(n):
    #         left_i = i
    #         right_i = i
    #         while left_i >= 0 and heights[left_i] >= heights[i]:
    #             left_i -= 1
    #         while right_i < n and heights[right_i] >= heights[i]:
    #             right_i += 1
    #
    #         ans = max(ans, (right_i - left_i - 1) * heights[i])
    #     return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop(-1)] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            ans = max(ans, heights[stack.pop(-1)] * (n - stack[-1] - 1))
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([1]))