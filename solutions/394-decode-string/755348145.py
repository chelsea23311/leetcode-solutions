class Solution(object):
    def decodeString(self, s):
        def backtrack(i):
            res=''
            num=0
            while i<len(s):
                if s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                elif s[i]=='[':
                    sub_str,i=backtrack(i+1)
                    res+=sub_str*num
                    num=0
                elif s[i]==']':
                    return res,i+1
                else:
                    res+=s[i]
                    i+=1
            return res,i
        res,_=backtrack(0)
        return res
                

                
                



        """
        :type s: str
        :rtype: str
        """
        