class Solution(object):
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        length=min(m,n)
        for index in range(length):
            row,col=index,index
            if matrix[row][col]==target:
                return True
            for i in range(1,n-col):
                if matrix[row][col+i]==target:
                    return True
                elif matrix[row][col+i]>target:
                    break
            for j in range(1,m-row):
                if matrix[row+j][col]==target:
                    return True
                elif matrix[row+j][col]>target:
                    break
               
        return False
            
                

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        