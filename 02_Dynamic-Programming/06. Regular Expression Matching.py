class Solution:
    # Method 1: Memoization / Top-down
    def isMatch_memo(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                # Don't use '*' or use '*'
                ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                ans = dfs(i + 1, j + 1)
            else:
                ans = False
            
            cache[(i, j)] = ans
            return ans
        
        return dfs(0, 0)
    
    # Method 2: DP / Bottom-up
    def isMatch_dp(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        
        dp[-1][-1] = True  # Empty string matches empty pattern
        
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        
        return dp[0][0]


# Test cases
solution = Solution()
test_cases = [
    ("aa", "a"),      # False
    ("aa", "a*"),     # True
    ("ab", ".*"),     # True
    ("aab", "c*a*b"), # True
    ("mississippi", "mis*is*p*."),  # False
    ("aaa", "a*a"),   # True
    ("", "a*"),       # True
    ("", ".*"),       # True
    ("abcd", "d*"),   # False
    ("aaa", "ab*a"),  # False
]

print("Testing Regular Expression Matching:")
print("=" * 70)
print("s\t\tpattern\t\tMemo\tDP")
print("=" * 70)

for s, pattern in test_cases:
    memo_result = solution.isMatch_memo(s, pattern)
    dp_result = solution.isMatch_dp(s, pattern)
    print(f"{s:10}\t{pattern:10}\t{memo_result}\t{dp_result}")
    if memo_result != dp_result:
        print(f"Warning: Different results for s='{s}', pattern='{pattern}'!")