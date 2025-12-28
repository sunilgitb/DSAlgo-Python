# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Step 1: Prefix product
        p = 1
        for i in range(1, n):
            p *= nums[i-1]
            output[i] *= p  # multiply prefix product
        
        # Step 2: Suffix product
        p = 1
        for i in range(n-2, -1, -1):
            p *= nums[i+1]
            output[i] *= p  # multiply suffix product
        
        return output

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]

# Time: O(N)
# Space: O(1)
