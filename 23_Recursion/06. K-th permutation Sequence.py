# https://leetcode.com/problems/permutation-sequence/
# https://www.youtube.com/watch?v=wT7gcXLYoao

''' 
We if we fix one element then there can be (n-1) factorial of permutations starting with that element.
with this concept find the indeces and keep andding and popping elements from arr.
'''
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        p = math.factorial(n-1)
        res = ''
        k -= 1
        while k > 0:
            i = k // p
            res += arr[i]
            arr.pop(i)
            k %= p
            n -= 1
            p //= n
            
        res += ''.join(arr)
        return res

# Driver code
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (3, 1),  # n=3, k=1 → "123"
        (3, 2),  # "132"
        (3, 3),  # "213"
        (3, 4),  # "231"
        (3, 5),  # "312"
        (3, 6),  # "321"
        (4, 9),  # "2314"
        (4, 24), # "4321"
        (1, 1),  # "1"
    ]
    
    print("Testing Permutation Sequence (k-th permutation of n numbers)")
    print("=" * 60)
    
    for n, k in test_cases:
        result = sol.getPermutation(n, k)
        print(f"n={n}, k={k:2d} → \"{result}\"")
    
    print("\n" + "=" * 60)
    print("Detailed walkthrough for n=3, k=4:")
    print("-" * 60)
    
    # Detailed walkthrough for n=3, k=4
    n, k = 3, 4
    print(f"Step-by-step calculation for n={n}, k={k}:")
    print()
    
   
   

# Time Complexity = O(N*N) ; we are traversing nums 1 time but POPPING ELEMENT FROM MIDDLE OF ARRAY TAKES O(N) TIME, AS AFTER POPPING ELEMENTS REARRANGE WITH NEW INDEX. 
# Time Complexity = O(N!) # if we consider the time taken by math.factorial function.
# Space Complexity = O(N) ;    for taking arr.