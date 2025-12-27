class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i == j == 0: 
                    dp[i][j] = True
                elif j == 0: 
                    dp[i][j] = False
                elif i == 0:
                    if p[j-1] == '*': 
                        dp[i][j] = dp[i][j-1]
                    else: 
                        dp[i][j] = False 
                else:
                    if p[j-1] == '?': 
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == '*': 
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] 
                    elif s[i-1] == p[j-1]: 
                        dp[i][j] = dp[i-1][j-1]
                    else: 
                        dp[i][j] = False
        
        return dp[-1][-1]


# Test cases
solution = Solution()
test_cases = [
    ("aa", "a"),      # False
    ("aa", "*"),      # True
    ("cb", "?a"),     # False
    ("adceb", "*a*b"),# True
    ("acdcb", "a*c?b"), # False
    ("", "*"),        # True
    ("", ""),         # True
    ("a", ""),        # False
    ("abc", "a?c"),   # True
    ("x", "?"),       # True
]

print("Testing Wildcard Matching:")
print("-" * 60)
for s, p in test_cases:
    result = solution.isMatch(s, p)
    print(f"s='{s}', p='{p}' -> {result}")