class Solution:
    def num_ways(self, n: int, k: int) -> int:
        memo = {}
        
        def solve(n):
            if n == 0:
                return 0
            if n == 1:
                return k
            if n == 2:
                return k + k * (k - 1)
            if k == 1:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = solve(n - 2) * (k - 1) + solve(n - 1) * (k - 1)
            return memo[n]
        
        return solve(n)


# Test cases
solution = Solution()

# Test 1
n1, k1 = 3, 2
print(f"n={n1}, k={k1}: {solution.num_ways(n1, k1)}")  # Expected: 6

# Test 2
n2, k2 = 1, 1
print(f"n={n2}, k={k2}: {solution.num_ways(n2, k2)}")  # Expected: 1

# Test 3
n3, k3 = 2, 3
print(f"n={n3}, k={k3}: {solution.num_ways(n3, k3)}")  # Expected: 9

# Test 4
n4, k4 = 4, 2
print(f"n={n4}, k={k4}: {solution.num_ways(n4, k4)}")  # Expected: 10

# Test 5
n5, k5 = 0, 5
print(f"n={n5}, k={k5}: {solution.num_ways(n5, k5)}")  # Expected: 0