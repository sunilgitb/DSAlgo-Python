from typing import List

class Solution:
    def __init__(self):
        self.count = 0
    
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.count
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)
            
            # Count reverse pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                self.count += j
            
            # Merge two sorted arrays
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1


# Test cases
solution = Solution()

# Test 1
nums1 = [1, 3, 2, 3, 1]
print("Test 1:", solution.reversePairs(nums1))  # Expected: 2

# Test 2
solution = Solution()  # Reset count
nums2 = [2, 4, 3, 5, 1]
print("Test 2:", solution.reversePairs(nums2))  # Expected: 3

# Test 3
solution = Solution()  # Reset count
nums3 = [5, 4, 3, 2, 1]
print("Test 3:", solution.reversePairs(nums3))  # Expected: 4

# Test 4
solution = Solution()  # Reset count
nums4 = [1, 2, 3, 4, 5]
print("Test 4:", solution.reversePairs(nums4))  # Expected: 0

# Test 5
solution = Solution()  # Reset count
nums5 = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647]
print("Test 5:", solution.reversePairs(nums5))  # Expected: 0

# Test 6
solution = Solution()  # Reset count
nums6 = [1]
print("Test 6:", solution.reversePairs(nums6))  # Expected: 0

# Test 7
solution = Solution()  # Reset count
nums7 = []
print("Test 7:", solution.reversePairs(nums7))  # Expected: 0

# Test 8
solution = Solution()  # Reset count
nums8 = [2, 1, 3]
print("Test 8:", solution.reversePairs(nums8))  # Expected: 1