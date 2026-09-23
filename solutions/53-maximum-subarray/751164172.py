class Solution(object):
    def maxSubArray(self, nums):
        max_sum=float('-inf')
        sum=0
        for i in range(len(nums)):
            sum=max(sum+nums[i],nums[i])
            max_sum=max(sum,max_sum)
        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        