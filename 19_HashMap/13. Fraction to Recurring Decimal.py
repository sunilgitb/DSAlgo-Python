# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n = numerator; d = denominator; res = ''
        if n < 0 and d < 0: n = n; d = d
        elif n < 0 or d < 0: n = abs(n); d = abs(d); res = '-'
        seenRem = {}
        res += str(n // d) 
        n = n % d
        if n == 0: return res if res != '-0' else '0'
        res += '.'
        
        while n != 0:
            n *= 10
            res += str(n // d)
            n = n % d
            if n in seenRem:
                res = res[:seenRem[n]] + '(' + res[seenRem[n]:] + ')'
                break
            seenRem[n] = len(res)
        
        return res
# Driver code
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (1, 2),     # 0.5
        (2, 1),     # 2
        (2, 3),     # 0.(6)
        (4, 333),   # 0.(012)
        (-50, 8),   # -6.25
        (7, -12),   # -0.58(3)
        (-1, -2147483648)  # 0.0000000004656612873077392578125
    ]
    
    for numerator, denominator in test_cases:
        result = sol.fractionToDecimal(numerator, denominator)
        print(f"{numerator}/{denominator} = {result}")

