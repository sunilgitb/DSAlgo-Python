# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        # Step 1: reverse the first part
        reverse(0, n-k-1)
        # Step 2: reverse the last k elements
        reverse(n-k, n-1)
        # Step 3: reverse the entire array
        reverse(0, n-1)

# ---------------- Driver Code ----------------
solution = Solution()
arr = [1,2,3,4,5,6,7,8,9,10]
solution.rotate(arr, 3)
print(arr)  # Output: [8,9,10,1,2,3,4,5,6,7]
