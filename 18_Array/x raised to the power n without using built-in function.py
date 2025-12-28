# https://leetcode.com/problems/powx-n/
# Using Binary Exponentiation

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        p = abs(n)

        while p > 0:
            if p % 2 == 1:
                res *= x
                p -= 1
            else:
                x *= x
                p //= 2

        return res if n >= 0 else 1 / res


# ================= DRIVER CODE =================
if __name__ == "__main__":
    solution = Solution()

    print(solution.myPow(2.0, 10))   # Output: 1024.0
    print(solution.myPow(2.0, -2))   # Output: 0.25
    print(solution.myPow(2.1, 3))    # Output: 9.261


# Time: O(log(n))     # as get devided each time
# Space: O(1)