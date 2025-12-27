from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def solve(root):
            if not root: 
                return None
            
            # If root value is less than low, entire left subtree and root are out of range
            # So we only keep the right subtree (which might have values >= low)
            if root.val < low:
                return solve(root.right)
            
            # If root value is greater than high, entire right subtree and root are out of range
            # So we only keep the left subtree (which might have values <= high)
            elif root.val > high:
                return solve(root.left)
            
            # Root is within range, recursively trim left and right subtrees
            else:
                root.left = solve(root.left)
                root.right = solve(root.right)
                return root
        
        return solve(root)

# Helper function to print tree
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Example
print("Trim a Binary Search Tree:")
print("Range: [1, 3]")
print("\nOriginal tree:")
print("""
      3
     / \\
    0   4
     \\
      2
     /
    1
""")

# Build the tree
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)

print("\nOriginal tree structure:")
print_tree(root)

solution = Solution()
trimmed_root = solution.trimBST(root, 1, 3)

print("\nTrimmed tree (range [1, 3]):")
print_tree(trimmed_root)

print("\nExplanation:")
print("1. Node 0 < 1 → removed, but its right subtree (2 with child 1) is kept")
print("2. Node 4 > 3 → removed")
print("3. Final tree contains nodes with values 1, 2, 3")
print("4. BST properties are maintained")