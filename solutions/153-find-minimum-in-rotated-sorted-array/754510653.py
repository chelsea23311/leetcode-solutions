class Solution(object):
    def findMin(self, nums):
        def check(left,right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<=nums[-1]:
                    right=mid-1
                else:
                    left=mid+1
            return nums[left]
        return check(0,len(nums)-1)



        """
        :type nums: List[int]
        :rtype: int
        """
        