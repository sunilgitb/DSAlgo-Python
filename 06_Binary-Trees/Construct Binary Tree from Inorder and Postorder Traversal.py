from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create dictionary for O(1) lookup of inorder indices
        inorder_index_dict = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the last element of postorder (which is always the root)
        self.root_index = len(postorder) - 1
        
        def build(l: int, r: int) -> Optional[TreeNode]:
            """Build tree for inorder[l:r+1]"""
            if l > r:
                return None
            
            # Create root from current postorder element
            root_val = postorder[self.root_index]
            root = TreeNode(root_val)
            self.root_index -= 1
            
            # Find position of root in inorder
            inorder_idx = inorder_index_dict[root_val]
            
            # Important: Build right subtree first, then left subtree
            # Because in postorder: left → right → root, so when we traverse
            # postorder backwards, we encounter right subtree before left subtree
            root.right = build(inorder_idx + 1, r)
            root.left = build(l, inorder_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)

# Helper function to verify by traversals
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

# Example
print("Construct Binary Tree from Inorder and Postorder Traversal:")
print("\nInput:")
print("Inorder:   [9, 3, 15, 20, 7]")
print("Postorder: [9, 15, 7, 20, 3]")

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

solution = Solution()
tree = solution.buildTree(inorder, postorder)

print(f"\nExpected tree structure:")
print("""
        3
       / \\
      9   20
         /  \\
        15   7
""")

print(f"\nVerification:")
print(f"Reconstructed tree inorder: {inorder_traversal(tree)}")
print(f"Reconstructed tree postorder: {postorder_traversal(tree)}")
print(f"Matches original inorder? {inorder_traversal(tree) == inorder}")
print(f"Matches original postorder? {postorder_traversal(tree) == postorder}")

print("\nConstruction process:")
print("1. Last element of postorder (3) is root")
print("2. Find 3 in inorder: [9, |3|, 15, 20, 7]")
print("3. Left subtree: inorder[0:0] = [9]")
print("4. Right subtree: inorder[2:4] = [15, 20, 7]")
print("5. For right subtree:")
print("   - Last of remaining postorder (20) is root")
print("   - Find 20 in inorder: [15, |20|, 7]")
print("   - Left of 20: [15], Right of 20: [7]")