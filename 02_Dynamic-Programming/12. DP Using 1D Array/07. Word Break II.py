# https://leetcode.com/problems/word-break-ii/

# Method-1:  DP + DFS

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = {i: [] for i in range(len(s))}

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dic[i].append(word)

        res = []
        if not dic[0]:
            return res

        def solve(i, path):
            if i >= len(s):
                res.append(path)
                return
            for word in dic[i]:
                if path == "":
                    solve(i + len(word), word)
                else:
                    solve(i + len(word), path + " " + word)

        solve(0, "")
        return res


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # Output: ['cats and dog', 'cat sand dog']

    print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    # Output: ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']


    
    
    
    
# Method-2: DP

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[""] for _ in range(n+1)]

        for i in range(1, n+1):
            arr = []
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    if i - len(word) == 0:
                        arr.append(word)
                    elif dp[i-len(word)] != [""]:
                        for st in dp[i-len(word)]:
                            arr.append(st + " " + word)
            dp[i] = arr

        return dp[-1]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # Output: ['cats and dog', 'cat sand dog']

    print(sol.wordBreak("leetcode", ["leet", "code"]))
    # Output: ['leet code']

    
    
    
    
# Method-3: DP + DFS (Similar to Method-1)

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n+1)]

        for i in range(1, n+1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    dp[i].append(word)

        res = []
        if not dp[-1]:
            return res

        def solve(i, path):
            if i <= 0:
                res.append(path)
                return
            for word in dp[i]:
                if not path:
                    solve(i - len(word), word)
                else:
                    solve(i - len(word), word + " " + path)

        solve(n, "")
        return res


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # Output: ['cats and dog', 'cat sand dog']
