# https://leetcode.com/problems/divide-two-integers/description/
# https://www.youtube.com/watch?v=pBD4B1tzgVc

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        n = abs(dividend)
        d = abs(divisor)
        res = 0
        while n >= d:
            t = 0
            while n >= (d << (t+1)):
                t += 1

            res += 1 << t
            n -= d << t

        return -res if (dividend < 0) ^ (divisor < 0) else res


# ---------------- Driver Code ----------------
solution = Solution()

print(solution.divide(10, 3))       # Expected output: 3
print(solution.divide(7, -3))       # Expected output: -2
print(solution.divide(-2147483648, -1))  # Expected output: 2147483647 (overflow case)
print(solution.divide(1, 1))        # Expected output: 1
print(solution.divide(-15, 2))      # Expected output: -7


# Time: O(log N)
# Space: O(1)
