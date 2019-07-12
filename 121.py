
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

from typing import List
class Solution:

    # 最大收益 = max(今天买入的最大收益，不在今天买入的最大收益)
    # def maxProfit(self, prices: List[int]) -> int:
    #     days = len(prices)
    #     if days < 2:
    #         return 0
    #     if days == 2:
    #         return max((prices[1] - prices[0]), 0)
    #
    #     todayPrice = prices.pop(0)
    #     maxSellerPrice = prices[0]
    #     for price in prices:
    #         if maxSellerPrice < price:
    #             maxSellerPrice = price
    #     maxCostToday = maxSellerPrice - todayPrice
    #     return max(maxCostToday, self.maxProfit(prices))


    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     minPrice = float('inf')
    #     maxBenifit = 0
    #     for i in range(0, n):
    #         if prices[i] < minPrice:
    #             minPrice = prices[i]
    #         elif (prices[i] - minPrice) > maxBenifit:
    #             maxBenifit = prices[i] - minPrice
    #
    #     return maxBenifit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 1] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(- prices[i], dp[i - 1][1])
        return dp[n - 1][0]



if __name__ == '__main__':
    s = Solution()
    # maxCost = s.maxProfit([7, 1, 5, 3, 6, 4])
    # print(maxCost)
    #
    # maxCost = s.maxProfit([7, 6, 4, 3, 1])
    # print(maxCost)

    maxCost = s.maxProfit([1, 2])
    print(maxCost)

