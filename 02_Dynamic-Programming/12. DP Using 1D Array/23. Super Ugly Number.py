from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        dp = [1] * n               # dp[i] stores the i-th super ugly number
        pointers = [0] * k          # pointers for each prime

        for i in range(1, n):
            # next candidates from each prime
            candidates = [dp[pointers[j]] * primes[j] for j in range(k)]
            dp[i] = min(candidates)  # choose the smallest

            # increment pointers for primes that were used
            for j in range(k):
                if candidates[j] == dp[i]:
                    pointers[j] += 1

        return dp[-1]

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    sol = Solution()
    print(sol.nthSuperUglyNumber(n, primes))  # Output: 32
