class Solution(object):
    def generateParenthesis(self, n):
        output=[]
        def backtrack(path,left,right):
            if left==n and right==n:
                output.append(path)
                return
            if left!=n:
                backtrack(path+'(',left+1,right)
            if right!=n and left!=right:
                backtrack(path+')',left,right+1)
        backtrack('(',1,0)
        return output
        """
        :type n: int
        :rtype: List[str]
        """
        