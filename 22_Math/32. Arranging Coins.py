# https://leetcode.com/problems/arranging-coins/
# https://samirpaulb.github.io/assets/arranging-coins-leetcode.png

# ---------- MATH - Time: O(1) ----------
# ---------- MATH - O(1) ----------
class SolutionMath:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n + 0.25)**0.5 - 0.5)

# ---------- BINARY SEARCH - O(log N) ----------
class SolutionBinary:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l, r = 0, (n+1)//2
        while l <= r:
            mid = l + (r - l)//2
            if mid*(mid+1)//2 <= n:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

# ----------------- Driver Code -----------------
test_cases = [5, 8, 3, 10]

print("Using Math approach:")
solver = SolutionMath()
for n in test_cases:
    print(f"n={n} -> {solver.arrangeCoins(n)}")

print("\nUsing Binary Search approach:")
solver = SolutionBinary()
for n in test_cases:
    print(f"n={n} -> {solver.arrangeCoins(n)}")
