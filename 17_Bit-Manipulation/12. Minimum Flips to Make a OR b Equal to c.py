# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            if (a & 1) | (b & 1) != (c & 1):
                if (c & 1) == 1:
                    res += 1
                else:
                    res += (a & 1) + (b & 1)
            a, b, c = a >> 1, b >> 1, c >> 1
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.minFlips(2, 6, 5))    # 3
print(solution.minFlips(4, 2, 7))    # 1
print(solution.minFlips(1, 2, 3))    # 0
print(solution.minFlips(0, 0, 0))    # 0
print(solution.minFlips(8, 3, 5))    # 3

      
# Time: O(1)
# Space: O(1)
