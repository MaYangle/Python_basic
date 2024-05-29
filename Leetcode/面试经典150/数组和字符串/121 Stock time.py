# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

# 示例 2：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #具体思路就是先设置两个参数 来记录最小值和最大利益
        #然后遍历所有的值，如果值小于当前记录的最小值 那么最小值就重新赋值
        #在遍历的同时，将当前值与最小值的差值与之前的最大利益比较 然后取其中更大的那个
        minprice = prices[0]
        maxprofit = 0
        '''假如我想知道到底哪一天买入 哪一天卖出'''
        '''buy_day = sell_day = 0  # 初始化买入和卖出日期

        for i, price in enumerate(prices):
            if price < minprice:
                minprice = price
                buy_day = i  # 更新买入日期
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
                sell_day = i  # 更新卖出日期

        return maxprofit, buy_day, sell_day  '''
        for price in prices:
            minprice = min(minprice,price)
            maxprofit = max(maxprofit,price-minprice)

        return maxprofit


# 创建Solution类的一个实例
solution = Solution()

# 调用maxProfit方法并传入股票价格列表
print(solution.maxProfit([6, 7, 3, 2, 5, 1, 4, 9]))  # 输出：8