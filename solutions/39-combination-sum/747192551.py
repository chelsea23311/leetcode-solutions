class Solution(object):
    def combinationSum(self, candidates, target):
        output=[]
        def backtrack(result,numbers):
            numbers=sorted(numbers)
            if result>target:
                return
            elif result==target and numbers not in output:
                output.append(numbers)
            else:
                for i in range(len(candidates)-1,-1,-1):
                    backtrack(result+candidates[i],numbers+[candidates[i]])
        backtrack(0,[])
        return output
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        