# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
#  
#
# 提示：
#
# 所有元素乘积之和不会溢出 32 位整数
# a.length <= 100000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        ans = [1] * n
        leftProduct = [1] * n
        rightProduct = [1] * n

        product = 1
        for i in range(n):
            product = a[i] * product
            leftProduct[i] = product

        product = 1
        for i in reversed(range(n)):
            product = a[i] * product
            rightProduct[i] = product

        for i in range(n):
            if i == 0:
                ans[i] = rightProduct[1]
            elif i == n - 1:
                ans[i] = leftProduct[n - 2]
            else:
                ans[i] = leftProduct[i - 1] * rightProduct[i + 1]
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.constructArr([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
