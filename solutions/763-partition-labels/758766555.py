class Solution(object):
    def partitionLabels(self, s):
        hashmap=[0]*26
        for i,c in enumerate(s):
            hashmap[ord(c)-ord('a')]=i
        output=[]
        start,end=0,hashmap[ord(s[0])-ord('a')]
        for i,c in enumerate(s):
            cur_end=hashmap[ord(c)-ord('a')]
            end=max(cur_end,end)
            if i == end:
                output.append(end-start+1)
                start=end+1
            
        return output



        """
        :type s: str
        :rtype: List[int]
        """
        