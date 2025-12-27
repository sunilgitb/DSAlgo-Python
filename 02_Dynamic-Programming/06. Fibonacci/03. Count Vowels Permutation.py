# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007
        
        # Initialize counts for strings of length 1
        a = e = i = o = u = 1
        
        # For each additional position (from 2 to n)
        for _ in range(1, n):
            # Next values based on allowed transitions
            new_a = e % MOD
            new_e = (a + i) % MOD
            new_i = (a + e + o + u) % MOD
            new_o = (i + u) % MOD
            new_u = a % MOD
            
            # Update for next iteration
            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u
        
        # Total valid strings of length n
        return (a + e + i + o + u) % MOD


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
n = 1
print(sol.countVowelPermutation(n))  # Output: 5  ("a", "e", "i", "o", "u")

# Example 2
n = 2
print(sol.countVowelPermutation(n))  # Output: 10

# Example 3
n = 5
print(sol.countVowelPermutation(n))  # Output: 68

# Example 4
n = 10
print(sol.countVowelPermutation(n))  # Output: 1730

# Example 5 (larger n)
n = 20
print(sol.countVowelPermutation(n))  # Output: 759959057