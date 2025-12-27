from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Calculate left height (following left children)
        left_height = self.get_left_height(root)
        # Calculate right height (following right children)
        right_height = self.get_right_height(root)
        
        # If left and right heights are equal, tree is perfect/full
        if left_height == right_height:
            # Number of nodes in perfect binary tree = 2^h - 1
            return 2 ** left_height - 1
        else:
            # Tree is not perfect, count recursively
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def get_left_height(self, node: Optional[TreeNode]) -> int:
        """Calculate height by following only left children."""
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def get_right_height(self, node: Optional[TreeNode]) -> int:
        """Calculate height by following only right children."""
        height = 0
        while node:
            height += 1
            node = node.right
        return height

# Example
print("Count Nodes in Complete Binary Tree:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\  /
    4   5 6
""")

# Build a complete binary tree (level 3, 6 nodes)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

solution = Solution()
result = solution.countNodes(root)

print(f"\nNumber of nodes: {result}")

print("\nCalculation process:")
print("1. At root (1):")
print("   Left height: follow 1→2→4 → height = 3")
print("   Right height: follow 1→3→None → height = 2")
print("   Heights not equal (3 ≠ 2), so count recursively")

print("\n2. At left subtree (2):")
print("   Left height: follow 2→4 → height = 2")
print("   Right height: follow 2→5 → height = 2")
print("   Heights equal (2 = 2), so use formula: 2² - 1 = 3 nodes")

print("\n3. At right subtree (3):")
print("   Left height: follow 3→6 → height = 2")
print("   Right height: follow 3→None → height = 1")
print("   Heights not equal (2 ≠ 1), so count recursively")

print("\n4. At left subtree of 3 (6):")
print("   Left height: follow 6→None → height = 1")
print("   Right height: follow 6→None → height = 1")
print("   Heights equal (1 = 1), so use formula: 2¹ - 1 = 1 node")

print("\n5. At right subtree of 3 (None): 0 nodes")

print("\nTotal calculation:")
print("Root count = 1")
print("Left subtree (2) = 3 nodes")
print("Right subtree (3) = 1 (from 6) + 0 (from None) + 1 (root 3) = 2 nodes")
print("Total = 1 + 3 + 2 = 6 nodes ✓")

print("\nTime complexity: O(log²n) = O((log 6)²) ≈ O(2.58)")
print("Naive approach would be O(n) = O(6)")