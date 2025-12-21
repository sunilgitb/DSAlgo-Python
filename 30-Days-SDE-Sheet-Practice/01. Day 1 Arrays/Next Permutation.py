# https://leetcode.com/problems/next-permutation/
''' 
Next Permutation = elemtnt Just Greater than the current element.
So find the elemnt from traversing from end. if nums[i] > nums[i-1] we can swap these and get the 
value. but there may any greater element in right. 
'''

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        sp = -1
        n = len(nums)

        # 1) Find the swap point
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                sp = i

        # If no swap point, reverse entire array
        if sp == -1:
            nums.reverse()
            return

        # 2) Find the rightmost element greater than nums[sp - 1]
        lsp = sp - 1
        rsp = sp
        for i in range(sp + 1, n):
            if nums[i] > nums[lsp]:
                rsp = i

        # 3) Swap
        nums[lsp], nums[rsp] = nums[rsp], nums[lsp]

        # 4) Reverse the suffix
        l, r = sp, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [1, 3, 2],
        [2, 3, 1]
    ]

    sol = Solution()

    for nums in test_cases:
        original = nums[:]
        sol.nextPermutation(nums)
        print(f"Next permutation of {original} -> {nums}")

# Time: O(N)
# Space: O(1)