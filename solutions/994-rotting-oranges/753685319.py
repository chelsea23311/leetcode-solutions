class Solution(object):
    def orangesRotting(self, grid):
        m,n=len(grid),len(grid[0])
        deque=[]
        def check(matrix):
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]==1:
                        return 1
            return 0
        def bfs():
            count=0
            while len(deque)!=0:
                size=len(deque)
                rot=False
                for _ in range(size):
                    i,j=deque.pop(0) 
                    for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=x<m and 0<=y<n and grid[x][y]==1:
                            grid[x][y]=2
                            deque.append((x,y))
                            rot=True
                if rot:
                    count+=1
            return count
                
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    deque.append((i,j))
        time=bfs()
        return time if not check(grid) else -1

                


        """
        :type grid: List[List[int]]
        :rtype: int
        """
        