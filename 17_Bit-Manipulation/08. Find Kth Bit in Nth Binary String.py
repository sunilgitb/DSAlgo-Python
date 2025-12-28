# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/


''' 
# Brute Force Solution
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def revinv(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == '0':
                    s[i] = '1'
                else:
                    s[i] = '0'
            s = ''.join(s)
            s = s[::-1]
            return s
        
        dp = ['0'] * n
        dp[0] = '0'
        for i in range(n):
            dp[i] = dp[i-1] + '1' + revinv(dp[i-1])
        
        return dp[-1][k-1]
# Time: O(n^2)
# Space: (n)
''' 


# Optimal Solution:
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/discuss/785548/JavaC++Python-O(1)-Solutions


class Solution:
    # Brute Force Solution
    def findKthBitBrute(self, n: int, k: int) -> str:
        def revinv(s):
            s = list(s)
            for i in range(len(s)):
                s[i] = '1' if s[i] == '0' else '0'
            s = ''.join(s)[::-1]
            return s
        
        dp = ['0'] * n
        dp[0] = '0'
        for i in range(1, n):
            dp[i] = dp[i-1] + '1' + revinv(dp[i-1])
        
        return dp[-1][k-1]

    # Optimal O(1) Solution
    def findKthBit(self, n: int, k: int) -> str:
        return str(k // (k & -k) >> 1 & 1 ^ k & 1 ^ 1)


# -------- Driver Code --------
solution = Solution()

print(solution.findKthBitBrute(3, 1))  # '0'
print(solution.findKthBitBrute(3, 4))  # '1'
print(solution.findKthBitBrute(4, 11)) # '1'

print(solution.findKthBit(3, 1))       # '0'
print(solution.findKthBit(3, 4))       # '1'
print(solution.findKthBit(4, 11))      # '1'

