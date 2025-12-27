# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(a: int, b: int, operator: str) -> int:
            if operator == "+": return a + b
            if operator == "-": return a - b
            if operator == "*": return a * b
        
        memo = {}
        
        def solve(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]
            
            res = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])
                    for a in left:
                        for b in right:
                            res.append(calc(a, b, expr[i]))
            
            memo[expr] = res
            return res
        
        return solve(expression)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
expression = "2-1-1"
print(sol.diffWaysToCompute(expression))  # Output: [0, 2]

# Example 2
expression = "2*3-4*5"
print(sol.diffWaysToCompute(expression))  # Output: [-34, -14, -10, -10, 10]

# Example 3
expression = "1+2*3"
print(sol.diffWaysToCompute(expression))  # Output: [7, 9]

# Example 4
expression = "1"
print(sol.diffWaysToCompute(expression))  # Output: [1]

# Example 5
expression = "11+23*34"
print(sol.diffWaysToCompute(expression))  # Output: [798, 792, 858]

# Example 6
expression = "2*3+4*5"
print(sol.diffWaysToCompute(expression))  # Output: [24, 34, 26]