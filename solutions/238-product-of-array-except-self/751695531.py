class Solution(object):
    def productExceptSelf(self, nums):
        pre=[1]*len(nums)
        sur=[1]*len(nums)
        pre_sum,sur_sum=1,1
        output=[]
        for i in range(len(nums)):
            pre_sum*=nums[i]
            pre[i]=pre_sum
        for i in range(len(nums)-1,-1,-1):
            sur_sum*=nums[i]
            sur[i]=sur_sum
        for i in range(len(nums)):
            if i==0:
                output.append(sur[i+1])
            elif i==len(nums)-1:
                output.append(pre[i-1])
            else:
                output.append(pre[i-1]*sur[i+1])
        return output

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        