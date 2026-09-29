class Solution(object):
    def spiralOrder(self, matrix):
        m,n=len(matrix),len(matrix[0])
        left,right=n,n
        up,down=m-1,m
        row,col=0,0
        output=[]
        output.append(matrix[row][col])
        while 1:
            if right==1 and len(matrix[0])!=1:
                break
            for i in range(1,right):
                output.append(matrix[row][col+i])
            col+=right-1
            right=left-1
            if down==1:
                break
            for i in range(1,down):
                output.append(matrix[row+i][col])
            row+=down-1
            down=up-1
            if left==1:
                break
            for i in range(1,left):
                output.append(matrix[row][col-i])
            col-=left-1
            left=right-1
            if n==1 or up==1:
                break
            for i in range(1,up):
                output.append(matrix[row-i][col])
            row-=up-1
            up=down-1
            
        return output

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        