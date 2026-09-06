class Solution(object):
    def subsets(self, nums):
        output=[]
        def backtrack(result,index):
            
            output.append(result)
            if index==len(nums):
                
                return
            for i in range(0,len(nums)-index):
                if index+i<len(nums):
                    backtrack(result+[nums[index+i]],index+i+1)
        backtrack([],0)
        return output
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        