# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# Splitting a String Into Descending Consecutive Values
# Problem: Check if we can split the string s into 2 or more substrings such that:
# - Each substring represents a positive integer without leading zeros.
# - The integers are in strictly descending consecutive order (each next is exactly 1 less than previous).

class Solution:
    def splitString(self, s: str) -> bool:
        s += "0"
        n = len(s)
        e, i, j, k, z = 0, 0, 1, 0, 0
        h = int(s)
        
        if n == 2 or h == 0:
            return False
        
        while j < n - 1:
            num1 = int(s[e:i + 1])
            num2 = int(s[i + 1:j + 1])
            
            k = num1 - num2
            if num1 == 0 and num2 == 0:
                k = 1
            
            if k == 1:
                if e == 0:
                    z = i
                e, i, j = i + 1, j, j + 1
            elif k > 1 and j != n - 2:
                j += 1
            else:
                e, i, z, j = 0, z + 1, z + 1, z + 2
        
        if k==1:
            return True
        else:
            return False
# Driver Code with test cases
solution = Solution()

s = "4321"
print(solution.splitString(s))  # True

s = "1234"
print(solution.splitString(s))  # False

s = "1311"
print(solution.splitString(s))  # True

s = "0081"
print(solution.splitString(s))  # False
