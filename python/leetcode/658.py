# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
#  
#
# 示例 2:
#
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
#  
#
# 说明:
#
# k 的值为正数，且总是小于给定排序数组的长度。
# 数组不为空，且长度不超过 104
# 数组里的每个元素与 x 的绝对值不超过 104
#  
#
# 更新(2017/9/19):
# 这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-k-closest-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = arr
        while len(res) > k:
            first = res[0]
            last = res[-1]
            if abs(first - x) <= abs(last - x):
                res = res[:-1]
            else:
                res = res[1:]
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert s.findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], 4, 5) == [3, 4, 6, 7]