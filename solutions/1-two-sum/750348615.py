class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for idx,number in enumerate(nums):
            target_num=target-number
            if target_num in hashmap:
                return [idx,hashmap[target_num]]
            hashmap[number]=idx
        return []
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        