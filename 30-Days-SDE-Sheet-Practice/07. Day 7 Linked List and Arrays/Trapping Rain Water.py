# https://leetcode.com/problems/trapping-rain-water/


'''
Find left and right boundary for the current element the keep addding the amount of
water above the current height to the result. 
'''

# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l <= r:
            if height[l] <= height[r]:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))
    # Expected Output: 6

    height = [4,2,0,3,2,5]
    print(sol.trap(height))
    # Expected Output: 9

    height = [1,0,1]
    print(sol.trap(height))
    # Expected Output: 1

    
# Time: O(N)
# Space: O(1)




# Method - 2
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftBoundary, rightBoundary = [0] * n, [0] * n 
        lMax, rMax, ans = height[0], height[-1], 0
        
        for i in range(n):
            lMax = max(lMax, height[i])
            leftBoundary[i] = lMax
        
        for i in range(n - 1, -1, -1):
            rMax = max(rMax, height[i])
            rightBoundary[i] = rMax
        
        for i in range(n):
            ans += min(leftBoundary[i], rightBoundary[i]) - height[i]
        
        return ans
    
# Time: O(N)
# Space: O(N)