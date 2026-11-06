class Solution(object):
    def generate(self, numRows):
        output=[]
        for i in range(1,numRows+1):
            row=[1]*i
            output.append(row)
            for j in range(1,i-1):
                output[i-1][j]=output[i-2][j-1]+output[i-2][j]
        return output
                



        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        