class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m,n=len(text1),len(text2)
        max_length=0
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                max_length=max(max_length,dp[i][j])
        return max_length        


        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        