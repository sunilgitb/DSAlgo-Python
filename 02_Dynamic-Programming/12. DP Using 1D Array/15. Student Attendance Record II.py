class Solution:
    def checkRecord(self, n: int) -> int:
        memo = {}
        mod = 10**9 + 7
        
        def solve(i, a, l):
            if a > 1 or l >= 3: 
                return 0

            if i == n:
                return 1

            key = (i, a, l)

            if key in memo:
                return memo[key]

            # Three possibilities: P, A, L
            ans = (
                solve(i+1, a, 0) +      # P: present
                solve(i+1, a+1, 0) +    # A: absent
                solve(i+1, a, l+1)      # L: late
            ) % mod

            memo[key] = ans
            return ans
        
        return solve(0, 0, 0)

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    solution = Solution()
    
    n1 = 2
    print(f"n = {n1} -> Total valid attendance records: {solution.checkRecord(n1)}")  
    # Expected: 8 ("PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL")
    
    n2 = 3
    print(f"n = {n2} -> Total valid attendance records: {solution.checkRecord(n2)}")  
    # Expected: 19
