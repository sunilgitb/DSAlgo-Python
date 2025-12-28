# https://leetcode.com/problems/ugly-number
# https://youtu.be/M0Zay1Qr9ws

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:  # Negative numbers and 0 are not ugly
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p  # Keep dividing by prime factors 2, 3, 5
        return n == 1  # If remaining n is 1, it’s ugly

# ---------------- Driver Code ----------------
if __name__ == "__main__":
    solution = Solution()
    nums = [6, 8, 14, 1, 0, -5]
    for num in nums:
        print(f"Is {num} ugly? {solution.isUgly(num)}")
