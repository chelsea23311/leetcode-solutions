class Solution(object):
    def maxProduct(self, nums):
        dp = [ [float('-inf'), float('inf')] for _ in range(len(nums)+1) ]
        dp[0]=[1,1]
        max_num=float('-inf')
        for idx,number in enumerate(nums):
            dp[idx+1][0]=max(dp[idx][0]*number,dp[idx][1]*number,number)
            dp[idx+1][1]=min(dp[idx][0]*number,dp[idx][1]*number,number)
            max_num=max(max_num,dp[idx+1][0])
        return max_num
        """
        :type nums: List[int]
        :rtype: int
        """
        