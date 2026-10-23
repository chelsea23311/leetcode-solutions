class Solution(object):
    def canJump(self, nums):
        max_far=0
        for i,num in enumerate(nums):
            if i > max_far:
                continue
            max_far=max(max_far,i+num)
        if max_far>=len(nums)-1:
            return True
        else:
            return False


        """
        :type nums: List[int]
        :rtype: bool
        """
        