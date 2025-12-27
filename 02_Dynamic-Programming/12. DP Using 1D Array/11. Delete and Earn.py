from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # This problem is SAME as House Robber I
        # We first convert nums into a value array where
        # value[i] = total points gained by deleting number i
        
        if not nums:
            return 0
        
        max_num = max(nums)
        arr = [0] * (max_num + 1)
        
        for num in nums:
            arr[num] += num
        # Example: nums = [2,2,3,3,3,4]
        # arr = [0, 0, 4, 9, 4]
        
        # Apply House Robber on arr
        n = len(arr)
        
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        
        return dp[-1]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()
    
    nums = [2, 2, 3, 3, 3, 4]
    print(sol.deleteAndEarn(nums))
    # Output: 9
