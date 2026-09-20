class Solution(object):
    def moveZeroes(self, nums):
        start=0
        index=0
        while index<len(nums):
            if nums[index] != 0:
                nums[start]=nums[index]
                start+=1
            index+=1
        for i in range(len(nums)-start):
            nums[start+i]=0
      
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        