# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & (1 << i):
                res |= (1 << (31 - i))
        return res


# -------- Driver Code --------
solution = Solution()

# Example 1: decimal input
n = 43261596
print(solution.reverseBits(n))  # 964176192

# Example 2: binary input
n = 0b101010  # same as decimal 42
print(solution.reverseBits(n))  # 1111490560
