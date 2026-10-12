class Solution(object):
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        def check(left,right):
            while left<=right:

                mid=(left+right)//2
                x,y=mid//n,mid%n
                if matrix[x][y]>target:
                    right=mid-1
                elif matrix[x][y]<target:
                    left=mid+1
                elif matrix[x][y]==target:
                    return True
            return False
        return check(0,n*m-1)
                
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        