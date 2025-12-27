from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        
        dp = defaultdict(int)
        streak = 0
        
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or (p[i-1] == 'z' and p[i] == 'a')):
                streak += 1
            else:
                streak = 1
            
            dp[p[i]] = max(dp[p[i]], streak)
        
        return sum(dp.values())


# Test cases
test_cases = [
    "a",          # Expected: 1
    "cac",        # Expected: 2  
    "zab",        # Expected: 6
    "abc",        # Expected: 6
    "abcd",       # Expected: 10
    "zabx",       # Expected: 7
    "",           # Expected: 0
    "aaaa",       # Expected: 4
    "abcdefghijklmnopqrstuvwxyz",  # Expected: 351
    "zabcdefghijklmnopqrstuvwxy",  # Expected: 351
]

solution = Solution()

print("Test Results:")
print("-" * 60)
for test in test_cases:
    result = solution.findSubstringInWraproundString(test)
    print(f"p = '{test}' : {result}")