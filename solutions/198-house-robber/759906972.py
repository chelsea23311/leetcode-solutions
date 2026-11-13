class Solution(object):
    def rob(self, nums):
        dp_first,dp_second=0,0
        for i in range(len(nums)):
            dp_k=max(dp_first+nums[i],dp_second)
            dp_first=dp_second
            dp_second=dp_k
            
        return dp_k


  
        """
        :type nums: List[int]
        :rtype: int
        """
        