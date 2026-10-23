class Solution(object):
    def maxProfit(self, prices):
        min_price=float('inf')
        max_profit=float('-inf')
        for price in prices:
            max_profit=max(price-min_price,max_profit)
            min_price=min(price,min_price)
        return max(max_profit,0)

        """
        :type prices: List[int]
        :rtype: int
        """
        