class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if i!=0 and j!=0:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

        """
        :type m: int
        :type n: int
        :rtype: int
        """
        