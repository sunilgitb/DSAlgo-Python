# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        logics = []
        stack = []
        
        def cal(tmp, top, op):
            if op == '!':
                tmp = 't' if tmp == 'f' else 'f'
            elif op == '&':
                tmp = 't' if (tmp == 't' and top == 't') else 'f'
            elif op == '|':
                tmp = 't' if (tmp == 't' or top == 't') else 'f'
            return tmp

        for i in expression:
            if i in ('!', '&', '|'):
                logics.append(i)
            elif i == ')':
                op = logics.pop()
                tmp = stack.pop()
                while stack:
                    top = stack.pop()
                    if op == '!' and top == '(':
                        tmp = cal(tmp, tmp, op)
                    if top == '(':
                        break
                    tmp = cal(tmp, top, op)
                stack.append(tmp)
            elif i == ',':
                continue
            else:
                stack.append(i)
        
        if logics:
            op = logics.pop()
            tmp = stack.pop()
            while stack:
                top = stack.pop()
                tmp = cal(tmp, top, op)
            stack.append(tmp)
        
        return stack[0] == 't'


# -------- Driver Code --------
solution = Solution()

print(solution.parseBoolExpr("!(f)"))          # True
print(solution.parseBoolExpr("|(f,t)"))        # True
print(solution.parseBoolExpr("&(t,f)"))        # False
print(solution.parseBoolExpr("|(&(t,f,t),!(t))"))  # False
