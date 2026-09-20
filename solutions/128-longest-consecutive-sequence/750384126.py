class Solution(object):
    def longestConsecutive(self, nums):
        nums=sorted(nums)
        maxlen=1
        if not nums:
            return 0
        cur_len=1
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                cur_len+=1
            else:
                cur_len=1
            maxlen=max(maxlen,cur_len)
        return maxlen
                

        """
        :type nums: List[int]
        :rtype: int
        """
        