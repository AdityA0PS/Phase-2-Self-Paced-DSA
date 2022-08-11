class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        length = len(cuts)
        cuts.sort()
        t = [[-1]*length for i in range(length)] 
        def solve(i, j, st, end):
            if st > end:
                return 0
            if t[st][end] != -1:
                return t[st][end]
            
            mn = sys.maxsize
            
            for k in range(st, end+1):
                temp = solve(i, cuts[k], st, k-1) + solve(cuts[k], j, k+1, end) + j-i
                
                if temp < mn:
                    mn = temp
            
            t[st][end] = mn
            return t[st][end]
        return solve(0, n, 0, length-1)