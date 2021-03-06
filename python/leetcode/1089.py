# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
#
# 注意：请不要在超过该数组长度的位置写入元素。
#
# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
#
#  
#
# 示例 1：
#
# 输入：[1,0,2,3,0,4,5,0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
# 示例 2：
#
# 输入：[1,2,3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1,2,3]
#  
#
# 提示：
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/duplicate-zeros
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        ans = [0] * n
        i = 0
        j = 0
        while j < n:
            if arr[i] == 0:
                j += 2
            else:
                ans[j] = arr[i]
                j += 1
            i += 1

        for i in range(n):
            arr[i] = ans[i]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    s.duplicateZeros(arr)
    assert arr == [1,0,0,2,3,0,0,4]
