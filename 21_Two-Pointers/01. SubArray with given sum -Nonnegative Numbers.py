# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# Function to find a continuous sub-array which adds up to a given number.

class Solution:
    def subArraySum(self,arr, n, s): 
        curSum = 0
        l = 0
        for r in range(n):
            curSum += arr[r]
            while curSum > s and l < r:
                curSum -= arr[l]
                l += 1
            if curSum == s: return [l+1, r+1]
        
        
if __name__ == "__main__":
    solution = Solution()
    
    arr = [1, 2, 3, 7, 5]
    n = len(arr)
    s = 12
    print(solution.subArraySum(arr, n, s))  # Output: [2, 4] (2+3+7=12)
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    s = 15
    print(solution.subArraySum(arr, n, s))  # Output: [1, 5] (1+2+3+4+5=15)
    
    arr = [1, 4, 20, 3, 10, 5]
    n = len(arr)
    s = 33
    print(solution.subArraySum(arr, n, s))  # Output: [3, 5] (20+3+10=33)

       
 