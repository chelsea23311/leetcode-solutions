class Solution(object):
    def lengthOfLIS(self, nums):
        dp=[1]*(len(nums))
        max_length=1
        for idx,number in enumerate(nums):
            for i in range(idx):
                if number>nums[i]:
                    dp[idx]=max(dp[idx],dp[i]+1)
            max_length=max(max_length,dp[idx])
        return max_length
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        