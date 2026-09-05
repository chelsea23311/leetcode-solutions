class Solution(object):
    def permute(self, nums):
        output=[]
        def backtrack(result,index):
            if index==len(nums):
                output.append(result)
                return
            for number in nums:
                if number in result:
                    continue
                
                backtrack(result+[number],index+1)
        
        backtrack([],0)
        return output

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        