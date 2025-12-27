from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten binary tree to linked list in-place.
        The linked list should use the right pointer and left should be None.
        """
        current = root
        
        while current:
            if not current.left:
                # No left child, move to right
                current = current.right
            else:
                # Find the rightmost node in left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Rewire connections
                # 1. Connect rightmost of left subtree to current's right subtree
                predecessor.right = current.right
                # 2. Move left subtree to right
                current.right = current.left
                # 3. Set left to None
                current.left = None
                # 4. Move to next node (original left child, now right child)
                current = current.right

# Helper function to print linked list
def print_linked_list(root):
    result = []
    current = root
    while current:
        result.append(current.val)
        current = current.right
    return result

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
print("Flatten Binary Tree to Linked List (Morris Traversal style):")
print("\nOriginal tree structure:")
print("""
        1
       / \\
      2   5
     / \\   \\
    3   4   6
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

print("\nOriginal tree:")
print_tree(root)

solution = Solution()
solution.flatten(root)

print("\nFlattened linked list structure:")
print("1 → 2 → 3 → 4 → 5 → 6 → None")

print("\nFlattened tree (as linked list):")
linked_list = print_linked_list(root)
print(f"Linked list values: {linked_list}")
print(f"All left pointers are None: {all(node.left is None for node in [root, root.right, root.right.right, root.right.right.right, root.right.right.right.right, root.right.right.right.right.right] if node)}")

print("\nStep-by-step transformation:")
print("1. Start at node 1:")
print("   - Find rightmost of left subtree (node 4)")
print("   - Connect 4.right to 1.right (5)")
print("   - Move left subtree to right: 1.right = 2")
print("   - Set 1.left = None")
print("   - Result: 1 → 2 → 3 → 4 → 5 → 6")

print("\n2. Move to node 2:")
print("   - Find rightmost of left subtree (node 3)")
print("   - Connect 3.right to 2.right (4)")
print("   - Move left subtree to right: 2.right = 3")
print("   - Set 2.left = None")
print("   - Result: 1 → 2 → 3 → 4 → 5 → 6")

print("\n3. Continue until all nodes processed...")
print("\nFinal flattened structure:")
current = root
while current:
    left_status = "None" if current.left is None else f"{current.left.val}"
    right_status = "None" if current.right is None else f"{current.right.val}"
    print(f"Node {current.val}: left={left_status}, right={right_status}")
    current = current.right