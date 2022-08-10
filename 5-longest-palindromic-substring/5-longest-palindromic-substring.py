class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        results = defaultdict(list)

        for idx in range(len(s)):
            for diff in [0, 1]:
                left = idx
                right = left + diff

                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                maxLen = max(maxLen, right - left - 1)
                results[maxLen].append([left + 1, right])
        
        i, j = results[maxLen][0]
        return s[i:j]