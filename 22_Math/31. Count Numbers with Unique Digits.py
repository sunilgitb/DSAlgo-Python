# https://leetcode.com/problems/count-numbers-with-unique-digits/

'''
n = 2
From 11 -> 20 => 11,22,33,..99 excluded. 
so ans = 10(for 1->10) + 9*9(as 1 element excluded in each 10 range). = 10 + 81 = 91

n = 3
for 1 -> 100 => ans = 91
From 101 -> 200 => (100,101), (110,112,113...119), (121,122),..(191,199) excluded.
ans(100, 199) = 8*9
From 201 -> 300 => (200,202), (211,212), (220,221,222...229),..(292,299) excluded.
ans(200, 299) = 8*9
.
.
ans(100, 1000) = 8*9*9
Total ans = 10 + 8*9*9 = 739

So Pattern = ans + 9*(11-i) ans i = [2,n]
'''

# https://leetcode.com/problems/count-numbers-with-unique-digits/
# Count Numbers with Unique Digits
# Problem: Given an integer n, return the count of all numbers with unique digits,
#          x where 0 <= x < 10^n.

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Optimal O(n) solution using combinatorics:
        - For 1 digit: 10 (0-9)
        - For 2 digits: 10 + 9×9 = 91
        - For 3 digits: 91 + 9×9×8 = 739
        - General pattern: ans += 9 × 9 × 8 × ... × (11-i)
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        ans = 10
        tmp = 9
        for i in range(2, n + 1):
            tmp *= (11 - i)  # 9, 8, 7, ...
            ans += tmp
        
        return ans


# Driver Code with test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (0, 1),    # 0 (only single 0)
        (1, 10),   # 0-9
        (2, 91),   # 0-99 excluding duplicates like 11,22,...
        (3, 739),  # 0-999
        (4, 5275), # 0-9999
        (5, 30249),
        (6, 136081),
        (7, 470185),
        (8, 1263225),
    ]
    
    print("Testing Count Numbers with Unique Digits\n" + "="*50)
    
    for idx, (n, expected) in enumerate(test_cases, 1):
        result = solution.countNumbersWithUniqueDigits(n)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: n = {n:2d} → {result} (Expected: {expected})")
        print("-" * 50)

# Dynamic Programming

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1, 10]
        for i in range(2, n+1):
            tmp = 81
            for j in range(1, i-1):
                tmp *= (9 - j)
            ans = dp[i-1] + tmp
            dp.append(ans)
        
        return dp[n]
                
