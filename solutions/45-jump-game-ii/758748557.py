class Solution(object):
    def jump(self, nums):
        end=0
        count=0
        max_length=0
        for i in range(len(nums)-1):
            max_length=max(max_length,i+nums[i])
            if i==end:
                count+=1
                end=max_length
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        