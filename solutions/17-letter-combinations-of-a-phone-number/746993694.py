class Solution(object):

    def letterCombinations(self, digits):
        map={'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }
        result=[]

        def backtrack(path,index):
            if index==len(digits):
                result.append(path)
                return 
            number=digits[index]
            for c in map[number]:
                backtrack(path+c,index+1)
        backtrack('',0)
        return result
        """
        :type digits: str
        :rtype: List[str]
        """
        
        