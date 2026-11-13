class Solution(object):
    def coinChange(self, coins, amount):
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for x in range(1,amount+1):
            for coin in coins:
                if x>=coin:
                    dp[x]=min(dp[x-coin]+1,dp[x])
        return dp[amount] if dp[amount] != float('inf') else -1
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        