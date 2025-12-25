# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class Solution:
    def findTarget(self, root, k):
        arr = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        l, r = 0, len(arr) - 1
        while l < r:
            twoSum = arr[l] + arr[r]
            if twoSum < k:
                l += 1
            elif twoSum > k:
                r -= 1
            else:
                return True
            
        return False


# Time: O(N)
# Space: O(N)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Construct BST
#        5
#       / \
#      3   6
#     / \   \
#    2   4   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

k = 9

solution = Solution()
print(solution.findTarget(root, k))
# Expected Output: True   (2 + 7 = 9)
