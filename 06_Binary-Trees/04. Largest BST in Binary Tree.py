class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def largestBst(self, root):
        def solve(root):
            # Returns: (isBST, min_val, max_val, size)
            if not root: 
                return True, float('inf'), float('-inf'), 0
            
            # Leaf node
            if not root.left and not root.right:
                return True, root.data, root.data, 1
            
            # Recursively check left and right subtrees
            lBST, lMin, lMax, lSize = solve(root.left)
            rBST, rMin, rMax, rSize = solve(root.right)
            
            # If both subtrees are BST and current node satisfies BST property
            if lBST and rBST and lMax < root.data < rMin:
                current_min = min(lMin, root.data)
                current_max = max(rMax, root.data)
                current_size = 1 + lSize + rSize
                return True, current_min, current_max, current_size
            else:
                # Current subtree is not BST, return the largest BST size found so far
                return False, 0, 0, max(lSize, rSize)
        
        return solve(root)[3]

# Example
print("Finding the largest BST in a binary tree:")
print("Tree structure:")
print("""
        10
       /  \\
      5    15
     / \\   / \\
    1   8 7   40
""")

# Build the tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(40)

solution = Solution()
result = solution.largestBst(root)
print(f"\nSize of the largest BST in the tree: {result}")

# Explanation
print("\nExplanation:")
print("• The subtree rooted at 5 (with nodes 1, 5, 8) is a BST of size 3")
print("• The subtree rooted at 15 (with nodes 7, 15, 40) is a BST of size 3") 
print("• The entire tree is NOT a BST because 7 < 10 (violates BST property)")
print(f"• Therefore, largest BST size is: {result}")