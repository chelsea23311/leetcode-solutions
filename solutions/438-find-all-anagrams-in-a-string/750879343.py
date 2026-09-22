class Solution(object):
    def findAnagrams(self, s, p):
        output=[]
        length=len(p)
        if length>len(s):
            return output
        hashmap=[0]*26
        visited=[0]*26
        for word in p:
            hashmap[ord(word)-ord('a')]+=1

        for i in range(length):
            visited[ord(s[i])-ord('a')]+=1
        if visited==hashmap:
                output.append(0)
        visited[ord(s[0])-ord('a')]-=1
        left=1
       
        while left<=len(s)-length:
            right=left+length-1
            visited[ord(s[right])-ord('a')]+=1
            if visited==hashmap:
                output.append(left)
            
            visited[ord(s[left])-ord('a')]-=1
            left+=1
           
             
        return output



            


        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        