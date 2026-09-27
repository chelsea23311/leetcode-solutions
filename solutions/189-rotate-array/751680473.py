class Solution(object):
    def rotate(self, nums, k):
        def reverse(l,r):
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        while k>len(nums):
            k=k%len(nums)
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)    

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        