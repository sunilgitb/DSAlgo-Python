# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        
        l = 0; r = len(nums)
        mid = l + (r-l) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

# Time Complexity = O(log(N)); as we are implmenting binary search where N = lec(nums) 
# Space COmplexity = O(N)  


if __name__ == "__main__":
   

    def inorder(root, out):
        if not root: return
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)

    # Example sorted array
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)

    out = []
    inorder(root, out)
    print("Inorder traversal of constructed BST:", out)
    # Expected output: [-10, -3, 0, 5, 9]
