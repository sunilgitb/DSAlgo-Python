from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        count = 0
        
        def dfs(node):
            """
            Return list of distances from current node to all leaf nodes in its subtree.
            Also update count of good pairs where LCA is current node.
            """
            nonlocal count
            
            if not node:
                return []
            
            # If leaf node, return [1] (distance 1 to itself)
            if not node.left and not node.right:
                return [1]
            
            # Get distances to leaves from left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count pairs where LCA is current node
            # Distance between leaves = left_distance + right_distance
            for left_dist in left_distances:
                for right_dist in right_distances:
                    if left_dist + right_dist <= distance:
                        count += 1
            
            # Return distances + 1 for parent, filter those that might still form valid pairs
            combined = []
            for dist in left_distances + right_distances:
                if dist + 1 < distance:  # +1 for edge to parent, < distance to potentially form valid pairs
                    combined.append(dist + 1)
            
            return combined
        
        dfs(root)
        return count

# Example
print("Count Good Leaf Nodes Pairs:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
         / \\
        4   5
       / \\   \\
      6   7   8
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(8)

distance = 3
solution = Solution()
result = solution.countPairs(root, distance)

print(f"\nDistance threshold: {distance}")
print(f"Number of good leaf pairs: {result}")

print("\nLeaf nodes: [2, 6, 7, 8]")
print("All leaf pairs and their distances:")
print("1. Pair (2, 6): Path 2→1→3→4→6 = 4 edges > 3 ✗")
print("2. Pair (2, 7): Path 2→1→3→4→7 = 4 edges > 3 ✗")
print("3. Pair (2, 8): Path 2→1→3→5→8 = 4 edges > 3 ✗")
print("4. Pair (6, 7): Path 6→4→7 = 2 edges ≤ 3 ✓")
print("5. Pair (6, 8): Path 6→4→3→5→8 = 4 edges > 3 ✗")
print("6. Pair (7, 8): Path 7→4→3→5→8 = 4 edges > 3 ✗")
print(f"\nTotal good pairs: 1 (only pair (6, 7))")

print("\nAlgorithm explanation:")
print("1. Post-order traversal (bottom-up)")
print("2. At each node, return distances to leaves in its subtree")
print("3. When processing a node, count pairs where:")
print("   - One leaf from left subtree")
print("   - One leaf from right subtree")
print("   - Distance = left_dist + right_dist ≤ threshold")
print("4. Propagate distances upward (+1 for parent edge)")

print("\nExecution at key nodes:")
print("Node 4 (parent of leaves 6 and 7):")
print("   left_distances = [1] (from leaf 6)")
print("   right_distances = [1] (from leaf 7)")
print("   Count pair: 1 + 1 = 2 ≤ 3 → count += 1")
print("   Return: [2, 2] (distances+1)")

print("\nNode 3 (parent of subtrees 4 and 5):")
print("   left_distances = [2, 2] (from node 4)")
print("   right_distances = [2] (from leaf 8 via node 5)")
print("   Check pairs: 2+2=4>3 ✗, 2+2=4>3 ✗, 2+2=4>3 ✗")
print("   No new pairs counted")