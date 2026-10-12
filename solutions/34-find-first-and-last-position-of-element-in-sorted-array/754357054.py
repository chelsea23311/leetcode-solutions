class Solution(object):
    def searchRange(self, nums, target):
        def check_first(left,right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return left
        
        def check_last(left,right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid -1
            return right
        
        L = check_first(0, len(nums)-1)
        R = check_last(0, len(nums)-1)
        if L >= len(nums) or nums[L] != target:
            return [-1,-1]
        return [L, R]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        