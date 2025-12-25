# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

from typing import List, Optional

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        parent = root
        stack = [parent]
        
        for v in preorder[1:]:
            newNode = TreeNode(v)
            if stack and newNode.val < parent.val:
                parent.left = newNode
                stack.append(newNode)
                parent = newNode
            else:
                while stack and stack[-1].val < newNode.val:
                    parent = stack.pop()
                parent.right = newNode
                stack.append(newNode)
                parent = newNode
        
        return root
    
    
# Time: O(N)
# Space: O(N)

if __name__ == "__main__":
    # Local TreeNode definition for example (matches LeetCode TreeNode)
   

    def inorder(root, out):
        if not root: return
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)

    # Example preorder (LeetCode example):
    preorder = [8, 5, 1, 7, 10, 12]
    root = Solution().bstFromPreorder(preorder)

    out = []
    inorder(root, out)
    print("Inorder traversal of constructed BST:", out)
    # Expected output: [1, 5, 7, 8, 10, 12]













































    