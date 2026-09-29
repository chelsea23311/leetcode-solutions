class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n//2):
            change=matrix[n-1-i]
            matrix[n-1-i]=matrix[i]
            matrix[i]=change
        for i in range(n):
            for j in range(i,n):
                change=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=change
        

        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        