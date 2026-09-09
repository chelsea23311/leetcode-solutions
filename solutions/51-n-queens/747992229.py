class Solution(object):
    def solveNQueens(self, n):
        output=[]
        def is_safe(k, col, path, n):
            for i in range(n):
                 for j in range(n):
                    if path[i][j] == 'Q' and (k == i or abs(k-i) == abs(col-j)):
                        return False
            return True

        def backtrack(col,path):
            if col==n:
                path=[''.join(row) for row in path ]
                output.append(path)
                return
            for k in range(n):
                if is_safe(k,col,path,n):
                    new_path = [row[:] for row in path]
                    new_path[k][col] = 'Q'
                    backtrack(col+1, new_path)
                

               
        path=[]
        for i in range(n):       
            rows = []              
            for j in range(n):    
                rows.append('.')
            path.append(rows)
       
        backtrack(0,path)
        return output
              
        """
        :type n: int
        :rtype: List[List[str]]
        """
        