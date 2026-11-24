class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        if 1 not in nums:
            return 1
        for i in range(n):
            if nums[i]>n or nums[i]<=0:
                nums[i]=1
        for i in range(n):
            a=abs(nums[i])-1
            nums[a]=-abs(nums[a])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
        """
        :type nums: List[int]
        :rtype: int
        """
        