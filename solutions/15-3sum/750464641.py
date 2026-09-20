class Solution(object):
    def threeSum(self, nums):
        output=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                if (nums[i]+nums[left]+nums[right])==0 and [nums[i],nums[left],nums[right]] not in output:
                    
                    output.append([nums[i],nums[left],nums[right]])
                    right-=1
                elif (nums[i]+nums[left]+nums[right])>0:
                   
                        right-=1
                else:
                    
                        left+=1
        return output
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        