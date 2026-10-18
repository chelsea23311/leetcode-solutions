class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        output=[0]*len(temperatures)
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                temp=stack.pop()
                output[temp]=i-temp
            stack.append(i)
        return output
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        