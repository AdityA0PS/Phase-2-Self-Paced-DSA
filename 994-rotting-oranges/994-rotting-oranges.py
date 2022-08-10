class Solution:
    def orangesRotting(self, grid):
        n, m, count = len(grid), len(grid[0]), 0

        stack, visited = [], set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    stack.append([i,j,0])
                    visited.add((i,j))

        while stack:
            x, y, time = stack.pop(0)

            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx,ny) not in visited:
                    count -= 1

                    if count == 0:
                        return time + 1

                    visited.add((nx,ny))
                    stack.append([nx,ny,time+1])

        return 0 if count == 0 else -1
        