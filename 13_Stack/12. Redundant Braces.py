# https://www.interviewbit.com/problems/redundant-braces/
# Check if the given expression has redundant braces

class Solution:
    def braces(self, A: str) -> int:
        stack = []
        
        for ch in A:
            if ch == ')':
                # Check if the matching '(' is immediately before ')'
                if stack and stack[-1] == '(':
                    return 1  # redundant: () or (something empty)
                
                # Check if there is at least one operator inside the parentheses
                has_operator = False
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in '+-*/':
                        has_operator = True
                
                # Pop the '('
                if stack:
                    stack.pop()
                
                # If no operator was found → redundant braces
                if not has_operator:
                    return 1
                
            else:
                # Push all other characters (operators, operands, '(')
                stack.append(ch)
        
        return 0  # No redundant braces found


# Driver Code
solution = Solution()
print(solution.braces("((a+b))"))  # Output: 1 (redundant)
print(solution.braces("(a+(b)/c)"))  # Output: 0 (not redundant)
print(solution.braces("(a+b*(c-d))"))  # Output: 0 (not redundant)
print(solution.braces("((a))"))  # Output: 1 (redundant)