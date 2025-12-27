# https://leetcode.com/problems/word-break/
# https://youtu.be/Sx9NNgInc3A

# Memoization
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def dfs(l, r):
            if l == len(s):
                return True
            if r == len(s):
                return False
            if (l, r) in memo:
                return memo[(l, r)]

            cur = s[l:r+1]
            if cur in wordSet:
                ans = dfs(r+1, r+1) or dfs(l, r+1)
            else:
                ans = dfs(l, r+1)

            memo[(l, r)] = ans
            return ans

        return dfs(0, 0)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("leetcode", ["leet", "code"]))
    # Output: True

    print(sol.wordBreak("applepenapple", ["apple", "pen"]))
    # Output: True

    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # Output: False


# DP
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        wordSet = set(wordDict)

        for i in range(n - 1, -1, -1):
            for word in wordSet:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break

        return dp[0]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("leetcode", ["leet", "code"]))
    # Output: True

    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # Output: False

        

        
# Bottom-Up
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("leetcode", ["leet", "code"]))
    # Output: True

    print(sol.wordBreak("applepenapple", ["apple", "pen"]))
    # Output: True

    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # Output: False

        

        
        
# Time: O(N^2)
# Space: O(N)
