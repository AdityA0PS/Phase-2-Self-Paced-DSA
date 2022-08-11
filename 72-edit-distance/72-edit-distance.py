class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {} # (i, j) : #minOperations
        m = len(word1)
        n = len(word2)
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                minOperations = dfs(i + 1, j + 1)
            else:
                minOperations = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            cache[(i, j)] = minOperations
            return cache[(i, j)]

        return dfs(0,0)