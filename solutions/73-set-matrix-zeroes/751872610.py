class Solution(object):
    def setZeroes(self, matrix):
        flags=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    flags.append([i,j])
        for index in flags:
            for i in range(len(matrix)):
                matrix[i][index[1]]=0
            for j in range(len(matrix[0])):
                matrix[index[0]][j]=0
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        