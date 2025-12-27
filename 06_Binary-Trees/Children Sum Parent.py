class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isSumProperty(self, root):
        """
        Check if tree satisfies children sum property:
        For every node, node.data = left.data + right.data
        (with None children treated as 0)
        """
        # Base cases
        if not root:
            return 1  # Empty tree trivially satisfies
        
        # Leaf node satisfies property
        if not root.left and not root.right:
            return 1
        
        # Get values of children (0 if None)
        left_val = root.left.data if root.left else 0
        right_val = root.right.data if root.right else 0
        
        # Check current node and recursively check subtrees
        if (root.data == left_val + right_val and 
            self.isSumProperty(root.left) and 
            self.isSumProperty(root.right)):
            return 1
        else:
            return 0

# Example
print("Check Children Sum Property in Binary Tree:")
print("\nTree 1: Satisfies property")
print("Tree structure:")
print("""
        10
       /  \\
      8    2
     / \\   /
    3   5 2
""")

# Build tree 1 (satisfies property)
root1 = Node(10)
root1.left = Node(8)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(5)
root1.right.left = Node(2)

solution = Solution()
result1 = solution.isSumProperty(root1)

print(f"\nTree 1 satisfies children sum property? {'Yes' if result1 == 1 else 'No'}")

print("\nVerification:")
print("Node 10: 10 = 8 + 2 ✓")
print("Node 8: 8 = 3 + 5 ✓")
print("Node 2: 2 = 2 + 0 (right child is None) ✓")
print("Node 3: Leaf (trivially satisfies) ✓")
print("Node 5: Leaf (trivially satisfies) ✓")
print("Node 2: Leaf (trivially satisfies) ✓")

print("\n" + "="*50)
print("\nTree 2: Does NOT satisfy property")
print("Tree structure:")
print("""
        10
       /  \\
      8    2
     / \\   
    3   4
""")

# Build tree 2 (does NOT satisfy property)
root2 = Node(10)
root2.left = Node(8)
root2.right = Node(2)
root2.left.left = Node(3)
root2.left.right = Node(4)  # 8 ≠ 3 + 4 (should be 7)

result2 = solution.isSumProperty(root2)
print(f"\nTree 2 satisfies children sum property? {'Yes' if result2 == 1 else 'No'}")

print("\nVerification:")
print("Node 10: 10 = 8 + 2 ✓")
print("Node 8: 8 ≠ 3 + 4 (7) ✗")
print("Node fails at node 8: 8 ≠ 3 + 4")