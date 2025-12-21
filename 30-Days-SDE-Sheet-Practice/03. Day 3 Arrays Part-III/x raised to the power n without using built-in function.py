# https://leetcode.com/problems/powx-n/
# Using Binary Exponentiation

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        p = abs(n)

        while p > 0:
            if p % 2 == 1:
                res *= x
            x *= x
            p //= 2

        return res if n >= 0 else 1 / res


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (2.0, 10),
        (2.1, 3),
        (2.0, -2),
        (5.0, 0),
        (1.5, 5)
    ]

    for x, n in test_cases:
        print(f"myPow({x}, {n}) = {sol.myPow(x, n)}")


# Time: O(log(n))     # as get devided each time
# Space: O(1)