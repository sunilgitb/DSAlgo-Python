# https://leetcode.com/problems/permutation-sequence/
# https://www.youtube.com/watch?v=wT7gcXLYoao

''' 
We if we fix one element then there can be (n-1) factorial of permutations starting with that element.
with this concept find the indeces and keep andding and popping elements from arr.
'''
import math
# https://leetcode.com/problems/permutation-sequence/
# https://www.youtube.com/watch?v=wT7gcXLYoao

'''
If we fix one element, then there are (n-1)! permutations starting with that element.
Using this idea, we find the correct index at each step and build the answer.
'''

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n + 1)]
        res = ""
        k -= 1  # convert to 0-based index

        while n > 0:
            fact = math.factorial(n - 1)
            idx = k // fact
            res += arr[idx]
            arr.pop(idx)
            k %= fact
            n -= 1

        return res


# -------- DRIVER CODE --------
sol = Solution()

print(sol.getPermutation(3, 3))
# Expected Output: "213"

print(sol.getPermutation(4, 9))
# Expected Output: "2314"

print(sol.getPermutation(3, 1))
# Expected Output: "123"

print(sol.getPermutation(4, 24))
# Expected Output: "4321"


# Time Complexity = O(N*N) ; we are traversing nums 1 time but POPPING ELEMENT FROM MIDDLE OF ARRAY TAKES O(N) TIME, AS AFTER POPPING ELEMENTS REARRANGE WITH NEW INDEX. 
# Time Complexity = O(N!) # if we consider the time taken by math.factorial function.
# Space Complexity = O(N) ;    for taking arr.