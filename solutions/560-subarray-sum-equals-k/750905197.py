class Solution(object):
    def subarraySum(self, nums, k):
        count,pre=0,0
        hashmap={}
        hashmap[0]=1
        for i in range(len(nums)):
            pre=pre+nums[i]
            target=pre-k
            if target in hashmap:
                count+=hashmap[pre-k]
            if pre not in hashmap:
                hashmap[pre]=1
            else:
                hashmap[pre]+=1
        return count


        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        