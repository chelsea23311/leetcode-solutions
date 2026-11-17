class Solution(object):
    def canPartition(self, nums):
        sum=0
        for number in nums:
            sum=sum+number
        if sum%2!=0:
            return False
        target=sum/2
        dp=[False]*(target+1)
        dp[0]=True
        for number in nums:
            for i in range(target,number-1,-1):
                if dp[i-number]==True:
                    dp[i]=True
        return dp[target]
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        