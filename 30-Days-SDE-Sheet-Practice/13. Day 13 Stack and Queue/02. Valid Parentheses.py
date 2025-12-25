# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if not stack: stack.append(i)
                
            elif stack[-1] == "(" and i == ")": stack.pop()
            
            elif stack[-1] == "{" and i == "}": stack.pop()
            
            elif stack[-1] == "[" and i == "]": stack.pop()
            
            else: stack.append(i)
        
        return len(stack) == 0
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the length of the string s.
# The algorithm iterates through each character in the string once, resulting in O(n) time complexity.
# In the worst case, all opening brackets are pushed onto the stack, leading to O(n) space complexity.  
# Example Usage:
sol = Solution()
print(sol.isValid("()"))          # Output: True
print(sol.isValid("()[]{}"))      # Output: True
print(sol.isValid("(]"))          # Output: False
print(sol.isValid("([)]"))        # Output: False
print(sol.isValid("{[]}"))        # Output: True  

