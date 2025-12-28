"""
File: Postfix to Infix.py

Problem:
Convert a postfix expression to an infix expression.

Reference:
https://www.geeksforgeeks.org/postfix-to-infix/
"""

# ------------------------------------------------------------
# Function to convert postfix to infix
# ------------------------------------------------------------

def postfix_to_infix(exp: str) -> str:
    stack = []
    operators = set("+-*/^")

    for ch in exp:
        # If operand, push to stack
        if ch not in operators:
            stack.append(ch)
        else:
            # Pop two operands
            op2 = stack.pop()
            op1 = stack.pop()

            # Form new infix expression
            new_expr = f"({op1}{ch}{op2})"
            stack.append(new_expr)

    # Final infix expression
    return stack[-1]


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        "ab+c*",
        "ab+cd-*",
        "ABC/-AK/L-*",
        "23*54*+9-"
    ]

    for exp in test_cases:
        print(f"Postfix : {exp}")
        print(f"Infix   : {postfix_to_infix(exp)}")
        print("-" * 40)


"""
Output:
Postfix : ab+c*
Infix   : ((a+b)*c)
----------------------------------------
Postfix : ab+cd-*
Infix   : ((a+b)*(c-d))
----------------------------------------
Postfix : ABC/-AK/L-*
Infix   : ((A-(B/C))*((A/K)-L))
----------------------------------------
Postfix : 23*54*+9-
Infix   : (((2*3)+(5*4))-9)
----------------------------------------
"""

# ------------------------------------------------------------
# Time Complexity: O(N)
# Space Complexity: O(N)
# ------------------------------------------------------------
