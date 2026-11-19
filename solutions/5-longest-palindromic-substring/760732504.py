class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        max_length=1
        s_max=s[0]
        if n<2:
            return s
        dp=[[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for j in range(1,n):
            for i in range(j):
                dp[i][j]=(s[i]==s[j]) and (j-i<=2 or dp[i+1][j-1]==True)
                if dp[i][j] and j-i+1>max_length:
                    max_length=j-i+1
                    s_max=s[i:j+1]
        return s_max
        

        """
        :type s: str
        :rtype: str
        """
        