class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        dp=[False]*(len(s)+1)
        
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j]==True and s[j:i] in word_set:
                    dp[i]=True
        return True if dp[len(s)] else False

        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        