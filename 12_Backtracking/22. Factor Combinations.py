# https://www.lintcode.com/problem/1308


from typing import List

class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        self.n = n
        res = []
        def solve(n, i, tmp):
            if n == 1:
                res.append(tmp)
                return 
            while i*i <= n:
                if n%i == 0:
                    solve(n//i, i, tmp + [i])
                i += 1
            if n < self.n:
                solve(n//n, n, tmp + [n])
        solve(self.n, 2, [])
        return res

# Driver Code:
solution = Solution()
print(solution.get_factors(12))  # Expected Output: [[2, 6], [2, 2, 3], [3, 4]]
print(solution.get_factors(15))  # Expected Output: [[3, 5]]
print(solution.get_factors(32))  # Expected Output: [[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [4, 8]]
# Time: O(sqrt(n) * log(n))    # https://algo.monster/liteproblems/254
# Space: O(m + log(n))         where m is the number of combinations of factors.
