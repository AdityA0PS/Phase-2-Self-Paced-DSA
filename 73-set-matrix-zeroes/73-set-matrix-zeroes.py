class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index=[]
        m=len(matrix)
        n=len(matrix[0])
        if m>0 and n>0:
            rows=[]
            cols=[]
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]==0:
                        index.append([i,j])

            for x in index:
                if x[0] not in rows:
                    for i in range(n):
                        matrix[x[0]][i]=0
                        rows.append(x[0])
                if x[1] not in cols:
                    for j in range(m):
                        matrix[j][x[1]]=0
                        cols.append(x[1])
        