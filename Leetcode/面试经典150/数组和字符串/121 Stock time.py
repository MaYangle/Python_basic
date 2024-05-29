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