class Solution(object):
    def searchInsert(self, nums, target):
        def check(left,right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                elif nums[mid]==target:
                    return mid
            return left
        return check(0,len(nums)-1)

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        