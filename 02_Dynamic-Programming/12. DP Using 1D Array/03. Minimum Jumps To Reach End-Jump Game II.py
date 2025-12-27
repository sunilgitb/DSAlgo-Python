# https://leetcode.com/problems/jump-game-ii/

# ----------------------  Dynamic Programming Approach => TLE  ---------------------------------
# https://youtu.be/cETfFsSTGJI
# O(N) Greedy Solution

class Solution:
    def jump(self, nums):
        l = r = 0
        jumps = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps

sol = Solution()

print(sol.jump([2, 3, 1, 1, 4]))
# Output: 2
# Explanation: 0 -> 1 -> 4

print(sol.jump([2, 3, 0, 1, 4]))
# Output: 2

print(sol.jump([1, 1, 1, 1]))
# Output: 3

    
# Time: O(n^2)
# Space: O(n)
# We can also find the path of min jumps if we store the j index during updating dp in another array
# then traverse from n-1 to 0 to find the path of min jumps 


# ----------------------  Greedy Approach => All Testcases Passed  --------------------------------
# https://www.youtube.com/watch?v=dJ7sWiOoK7g
class Solution:
    def jump(self, nums):
        l = 0
        r = 0
        res = 0
        
        while r < len(nums) - 1:
            maxReachableIndex = 0
            for i in range(l, r+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            l = r + 1
            r = maxReachableIndex
            res += 1
        
        return res
    
# Time Complexity: O(N); as the inner for loop is also increasing r so intotal one loop
# Space Complexity: O(1)