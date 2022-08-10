class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [[""]]
        for _ in range(len(s)):
            dp.append([])

        
        for i in range(1, len(s)+1):
            for word in wordDict:
                k = len(word)
                if i-k < 0:
                    continue
                if word == s[i-k:i]:
                    for combo in dp[i-k]:
                        dp[i].append(combo+(" " if combo else "")+word)
                    
        return dp[-1]