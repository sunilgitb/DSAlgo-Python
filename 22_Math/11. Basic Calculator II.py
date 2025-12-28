# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # remove spaces
        stack = []
        sign = "+"
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # truncate towards 0
            elif s[i] in "+-*/":
                sign = s[i]
            i += 1

        return sum(stack)


# ----------------- Driver Code -----------------
sol = Solution()

expressions = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "14-3/2"
]

for expr in expressions:
    print(f"Expression: {expr} => Result: {sol.calculate(expr)}")
