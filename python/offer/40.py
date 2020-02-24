# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#  
#
# 限制：
#
# 0 <= k <= arr.length <= 1000
# 0 <= arr[i] <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        ns = [-1] * 10001
        ans = []
        for n in arr:
            ns[n] = ns[n] + 1

        for (i, n) in enumerate(ns):
            if len(ans) >= k:
                break
            if n >= 0:
                ans += ([i] * (n + 1))
        return ans[:k]