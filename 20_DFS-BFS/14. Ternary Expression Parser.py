# https://www.lintcode.com/problem/887/
# https://leetcode.com/problems/ternary-expression-parser/description/


class Solution:
    def parse_ternary(self, expression: str) -> str:
        def dfs(l, r):
            if l == r: return expression[l]
            cnt = 0
            for i in range(l, r+1):
                if expression[i] == "?":
                    cnt += 1
                elif expression[i] == ":":
                    cnt -= 1
                    if cnt == 0:
                        break 
            if expression[l] == "F": 
                return dfs(i+1, r)
            else: 
                return dfs(l+2, i-1)
        
        return dfs(0, len(expression)-1)

# Time: O(N)
if __name__ == "__main__":
    solution = Solution()

    expr1 = "T?2:3"
    print(solution.parse_ternary(expr1))  # Output: 2

    expr2 = "F?1:T?4:5"
    print(solution.parse_ternary(expr2))  # Output: 4

    expr3 = "T?T?F:5:3"
    print(solution.parse_ternary(expr3))  # Output: F
