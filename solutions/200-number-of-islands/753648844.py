class Solution(object):
    def numIslands(self, grid):
        count=0
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if grid[i][j]=='0':
                return
            else:
                grid[i][j]='0'
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<m and 0<=y<n:
                    dfs(x,y)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count
                        


        """
        :type grid: List[List[str]]
        :rtype: int
        """
        