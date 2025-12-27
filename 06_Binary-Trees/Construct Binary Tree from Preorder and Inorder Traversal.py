from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create dictionary for O(1) lookup of inorder indices
        inorder_index_dict = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the first element of preorder (which is always the root)
        self.root_index = 0
        
        def build(l: int, r: int) -> Optional[TreeNode]:
            """Build tree for inorder[l:r+1]"""
            if l > r:
                return None
            
            # Create root from current preorder element
            root_val = preorder[self.root_index]
            root = TreeNode(root_val)
            self.root_index += 1
            
            # Find position of root in inorder
            inorder_idx = inorder_index_dict[root_val]
            
            # Build left subtree first, then right subtree
            # Because in preorder: root → left → right
            # So when we traverse preorder forwards, we encounter left subtree before right
            root.left = build(l, inorder_idx - 1)
            root.right = build(inorder_idx + 1, r)
            
            return root
        
        return build(0, len(inorder) - 1)

# Helper function to verify by traversals
def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# Example
print("Construct Binary Tree from Preorder and Inorder Traversal:")
print("\nInput:")
print("Preorder: [3, 9, 20, 15, 7]")
print("Inorder:  [9, 3, 15, 20, 7]")

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

print(f"\nExpected tree structure:")
print("""
        3
       / \\
      9   20
         /  \\
        15   7
""")

print(f"\nVerification:")
print(f"Reconstructed tree preorder: {preorder_traversal(tree)}")
print(f"Reconstructed tree inorder: {inorder_traversal(tree)}")
print(f"Matches original preorder? {preorder_traversal(tree) == preorder}")
print(f"Matches original inorder? {inorder_traversal(tree) == inorder}")

print("\nConstruction process:")
print("1. First element of preorder (3) is root")
print("2. Find 3 in inorder: [9, |3|, 15, 20, 7]")
print("3. Left subtree: inorder[0:0] = [9]")
print("4. Right subtree: inorder[2:4] = [15, 20, 7]")
print("5. For right subtree:")
print("   - Next in preorder (20) is root")
print("   - Find 20 in inorder: [15, |20|, 7]")
print("   - Left of 20: [15], Right of 20: [7]")