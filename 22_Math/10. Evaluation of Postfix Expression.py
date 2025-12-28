# https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1/#

class Solution:
    def evaluatePostfix(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch in "*/+-":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculate(a, b, ch))
            else:
                stack.append(int(ch))  # convert character digit to integer
        
        return stack[0]  # final result

    def calculate(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b  # integer division


# -------------------------
# Example Usage
# -------------------------
expressions = [
    "231*+9-",   # evaluates to -4
    "123*+",     # evaluates to 7
    "82/"        # evaluates to 4
]

sol = Solution()
for exp in expressions:
    print(sol.evaluatePostfix(exp))

# Output:
# -4
# 7
# 4
