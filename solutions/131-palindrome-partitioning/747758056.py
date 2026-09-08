class Solution(object):
    def partition(self, s):
        output=[]
        def backtrack(start,path):
            if start==len(s):
                output.append(path)  
            for i in range(0,len(s)-start):
                sub = s[start : start + i + 1]
                if sub == sub[::-1]:
                    backtrack(start + i + 1, path + [sub])

        backtrack(0,[])
        return output
        """
        :type s: str
        :rtype: List[List[str]]
        """
        