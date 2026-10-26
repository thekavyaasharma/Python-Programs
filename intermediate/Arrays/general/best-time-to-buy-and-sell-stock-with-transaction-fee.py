# 714. Best Time to Buy and Sell Stock with Transaction Fee - Medium
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        buy = -prices[0]
        sell = 0
        for p in prices:
            buy = max(buy,sell-p)
            sell = max(sell,buy+p-fee)
        return sell
        