class Solution:
    def solve(self,i,j,a,dp):
        if i==0 and j==0:
            return a[0][0]
        if i<0 or j<0:
            return 1000000000000
        if dp[i][j]!=-1:
            return dp[i][j]
        
        up = a[i][j] + self.solve(i-1,j,a,dp)
        down = a[i][j] + self.solve(i,j-1,a,dp)
        dp[i][j] = min(up,down)
        return dp[i][j]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n)] for j in range(m)]
        return self.solve(m-1,n-1,grid,dp)