class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n  # dp[i] stores the i-th ugly number
        p2 = p3 = p5 = 0  # pointers for multiples of 2, 3, 5
        
        for i in range(1, n):
            # next possible multiples
            twoMultiple = dp[p2] * 2
            threeMultiple = dp[p3] * 3
            fiveMultiple = dp[p5] * 5
            
            # choose the smallest one
            dp[i] = min(twoMultiple, threeMultiple, fiveMultiple)
            
            # move the pointers if they were used
            if dp[i] == twoMultiple: p2 += 1
            if dp[i] == threeMultiple: p3 += 1
            if dp[i] == fiveMultiple: p5 += 1
        
        return dp[-1]

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    n = 10
    sol = Solution()
    print(sol.nthUglyNumber(n))  # Output: 12
