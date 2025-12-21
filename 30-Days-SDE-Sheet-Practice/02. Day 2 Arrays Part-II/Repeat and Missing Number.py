# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# https://www.codingninjas.com/codestudio/problems/873366
# https://youtu.be/5nMGY4VUoRY

'''
[1, 2, 3, 4, 5, 6]
arr = [1, 2, 3, 4, 6, 6]
lets 5 = x; 6 = y

1 + 2 + 3 + 4 + x + y = s        --eq(1)
1 + 2 + 3 + 4 + x + x = s1       --eq(2)
s = n(n+1)/2
s1 = sum(arr)

eq(2) - eq(1)
x - y = s - s1      --eq(3)

1^2 + 2^2 + 3^2 + 4^2 + x^2 + y^2 = p   --eq(4)
1^2 + 2^2 + 3^2 + 4^2 + x^2 + x^2 = p1   --eq(5)
p = n(n+1)(2n+1)/6

ep(5) - ep(4)
x^2 - y^2 = p - p1     
(x+y)(x-y) = p - p1 --eq(6)

use eq(3) in eq(6)
x + y = (p - p1) / (s - s1)     --eq(7)

eq(3) + eq(7)
2x = s - s1 + (p - p1) / (s - s1)
x = (s - s1 + (p - p1) / (s - s1)) // 2
'''

class Solution:
    def repeatedNumber(self, arr):
        n = len(arr)
        s = n * (n + 1) // 2      # Sum of first n numbers
        s1 = sum(arr)             # Sum of array elements

        p = n * (n + 1) * (2*n + 1) // 6  # Sum of squares of first n numbers

        for i in arr:
            p -= i**2             # p now = sum_squares_expected - sum_squares_actual

        diff = -p                  # x^2 - y^2

        x = (s1 - s + diff // (s1 - s)) // 2  # repeated number
        y = s - s1 + x                        # missing number
        
        return (x, y)

# Example usage
arr = [1, 2, 3, 4, 6, 6]
sol = Solution()
repeat, missing = sol.repeatedNumber(arr)
print("Repeated Number:", repeat)
print("Missing Number:", missing)

    # Time: O(n)
    # Space: O(1)