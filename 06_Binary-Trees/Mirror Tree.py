from typing import Optional

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def mirror(self, root):
        """
        Convert a binary tree to its mirror.
        Mirror of a tree: swap left and right children recursively.
        """
        def solve(root):
            if not root:
                return
            
            # Recursively mirror left and right subtrees
            solve(root.left)
            solve(root.right)
            
            # Swap left and right children
            root.left, root.right = root.right, root.left
        
        solve(root)
        return root

# Helper function to print tree
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.data))
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
print("Mirror (Invert) a Binary Tree:")
print("\nOriginal tree structure:")
print("""
        1
       / \\
      3   2
         / \\
        5   4
""")

# Build the original tree
root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(4)

print("\nOriginal tree:")
print_tree(root)

solution = Solution()
mirrored_root = solution.mirror(root)

print("\nMirrored tree structure:")
print("""
        1
       / \\
      2   3
     / \\
    4   5
""")

print("\nMirrored tree:")
print_tree(mirrored_root)

print("\nStep-by-step mirroring process:")
print("1. Start at leaves: Node 5 and 4 swap (but they're leaves, so no change)")
print("2. Move up: Node 2 swaps its children → left becomes 5, right becomes 4")
print("3. Move up: Node 3 (leaf) stays as is")
print("4. Root: Node 1 swaps its children → left becomes 2, right becomes 3")
print("5. Final tree structure is mirror of original")

print("\nVisual comparison:")
print("Original:  1      Mirrored:  1")
print("          / \\              / \\")
print("         3   2            2   3")
print("            / \\          / \\")
print("           5   4        4   5")