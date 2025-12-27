from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root):
            if not root: 
                return 0
            
            # Get excess coins from left and right subtrees
            left_excess = solve(root.left)
            right_excess = solve(root.right)
            
            # Add moves required to balance left and right subtrees
            self.res += abs(left_excess) + abs(right_excess)
            
            # Return total excess coins at current node
            # root.val - 1 is excess at current node
            # + left_excess + right_excess is excess from children
            return left_excess + right_excess + root.val - 1
        
        solve(root)
        return self.res

# Example
print("Distribute Coins in Binary Tree:")
print("Initial tree with coin distribution:")
print("""
        0
       / \\
      0   0
     /     \\
    0       0
""")
print("Coins at each node: [3,0,0,0,2]")

# Build the tree
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.right.right = TreeNode(0)

# Set coin values (different from node structure)
# Node 1 (root): 3 coins
# Node 2: 0 coins  
# Node 3: 0 coins
# Node 4: 0 coins
# Node 5: 2 coins
root.val = 3
root.left.val = 0
root.right.val = 0
root.left.left.val = 0
root.right.right.val = 2

solution = Solution()
result = solution.distributeCoins(root)

print(f"\nMinimum moves required: {result}")
print("\nExplanation:")
print("Total coins = 3 + 0 + 0 + 0 + 2 = 5")
print("Total nodes = 5")
print("Each node should have 1 coin")
print("Moves:")
print("1. Move 2 coins from root (node 1) to node 2: 2 moves")
print("2. Move 1 coin from root to node 3: 1 move")
print("3. Move 1 coin from node 5 to node 4: 1 move")
print("Total moves = 2 + 1 + 1 = 4")