class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out=[[1]]           
        
        for i in range(1, numRows):
            temp=[1]
            for j in range(1, i):
                temp.append(out[i-1][j-1] + out[i-1][j])
            temp.append(1)
            out.append(temp)
        return out
        