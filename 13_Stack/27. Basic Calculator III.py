# https://www.lintcode.com/problem/849/
# https://leetcode.com/problems/basic-calculator-iii/description/
# https://medium.com/@CalvinChankf/solving-basic-calculator-i-ii-iii-on-leetcode-74d926732437


# Approach 1 ----- SAME as Basic Calculator I Approach 1 ------------------------------

import collections
class Solution:
    def calculate(self, s: str) -> int:
        def helper(q):
            stack = []
            sign = '+'
            num = 0
            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num*10 + int(c)
                if c == '(':
                    num = helper(q)
                if c in '+-*/)' or not q:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop()/num))
                    sign = c
                    num = 0
                    if c == ')':
                        break
            return sum(stack)
                    

        q = collections.deque()
        for c in s:
            q.append(c)
        return helper(q)

# Driver Code:
s = Solution()
print(s.calculate("1 + 1"))                # Output: 2
print(s.calculate(" 6-4 / 2 "))            # Output: 4
print(s.calculate("2*(5+5*2)/3+(6/2+8)"))  # Output: 21
print(s.calculate("(2+6* 3+ 5- (3*14/7+2)*5)+3"))  # Output: -12
print(s.calculate("0"))                     # Output: 0
# Time: O(N)
# Space: O(N)