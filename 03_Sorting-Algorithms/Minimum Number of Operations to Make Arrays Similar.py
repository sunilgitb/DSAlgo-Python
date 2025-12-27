from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = sorted([i for i in nums if i % 2 == 1])
        nums_even = sorted([i for i in nums if i % 2 == 0])
        
        target_odd = sorted([i for i in target if i % 2 == 1])
        target_even = sorted([i for i in target if i % 2 == 0])
        
        res = 0
        for n, t in zip(nums_odd, target_odd):
            if n > t: 
                res += n - t
        for n, t in zip(nums_even, target_even):
            if n > t: 
                res += n - t
        
        return res // 2


# Test cases
solution = Solution()

# Test 1
nums1 = [8,12,6]
target1 = [2,14,10]
print("Test 1:", solution.makeSimilar(nums1, target1))  # Expected: 2

# Test 2
nums2 = [1,2,5]
target2 = [4,1,3]
print("Test 2:", solution.makeSimilar(nums2, target2))  # Expected: 1

# Test 3
nums3 = [1,1,1,1,1]
target3 = [1,1,1,1,1]
print("Test 3:", solution.makeSimilar(nums3, target3))  # Expected: 0

# Test 4
nums4 = [3,5,2,6]
target4 = [2,3,4,7]
print("Test 4:", solution.makeSimilar(nums4, target4))  # Expected: 1

# Test 5
nums5 = [10,20,30]
target5 = [5,25,35]
print("Test 5:", solution.makeSimilar(nums5, target5))  # Expected: 5