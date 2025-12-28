# https://leetcode.com/problems/number-of-1-bits/
# https://youtu.be/5Km3utixwZs


class Solution:
    # Method 1: Check each bit using AND and shift
    def hammingWeight1(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += n & 1
            n = n >> 1
        return res

    # Method 2: Check each bit using modulo and shift
    def hammingWeight2(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += n % 2
            n = n >> 1
        return res

    # Method 3: Brian Kernighan’s algorithm
    def hammingWeight3(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)  # remove the last set bit
            res += 1
        return res


# -------- Driver Code --------
solution = Solution()

nums = [0b00000000000000000000000000001011, 0b11111111111111111111111111111101, 11, 4294967293]

for n in nums:
    print("Input:", n)
    print("Method 1:", solution.hammingWeight1(n))
    print("Method 2:", solution.hammingWeight2(n))
    print("Method 3:", solution.hammingWeight3(n))
    print("-----")
