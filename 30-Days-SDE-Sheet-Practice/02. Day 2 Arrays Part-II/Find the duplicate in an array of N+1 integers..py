# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=32Ll35mhWg0

'''
Intuition: 
Use the 2 pointers approach of LinkedList Cycle problem. 
Since there is a duplicate number, we can always say that cycle will be formed.

The slow pointer moves by one step and the fast pointer moves by 2 steps and there exists a cycle so the first collision is bound to happen.

Then start a check pointer from 0 and another pointer from current slow's position.
The value where both collide will be the duplicate element.
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entry point of cycle (duplicate)
        check = 0
        while True:
            slow = nums[slow]
            check = nums[check]
            if slow == check:
                return check


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
        [1, 1, 2],
        [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    ]

    for i, nums in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print("Array:", nums)
        print("Duplicate Number:", sol.findDuplicate(nums))
        print("-" * 35)

# Time: O(n)
# Space: O(1)

'''
Let’s assume the distance between the first element and the first collision is a. 
So slow pointer has traveled a distance while fast(since moving 2 steps at a time) 
has traveled 2a distance. For slow and a fast pointer to collide 2a-a=a should be 
multiple of the length of cycle, Now we place a fast pointer to start.
Assume the distance between the start and duplicate to be x. 
So now the distance between slow and duplicate shows also be x, as seen from the diagram,
and so now fast and slow pointer both should move by one step.
'''