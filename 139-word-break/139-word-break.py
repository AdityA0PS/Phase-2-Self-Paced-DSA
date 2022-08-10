class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:
                    res[i] = res[i-len(word)] or res[i]
        return res[-1]