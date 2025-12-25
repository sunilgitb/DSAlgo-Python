# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

'''
Traverse from bottom to top (Postorder Traversal).

For each node:
- Collect distances of all leaf nodes in its left and right subtrees.
- When both subtrees exist, check all (left, right) pairs.
- If l + r <= distance → good pair.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            
            if not node:
                return []
            
            # Leaf node
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Count good pairs
            count += sum(l + r <= distance for l in left for r in right)
            
            # Return incremented distances (pruning those >= distance)
            return [d + 1 for d in left + right if d + 1 < distance]
        
        dfs(root)
        return count


# Time Complexity: O(N)
# Space Complexity: O(N)
# Construct Tree
#        1
#       / \
#      2   3
#     /     \
#    4       5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

distance = 4   # FIXED

solution = Solution()
print(solution.countPairs(root, distance))
# Expected Output: 1

# Expected Output: 1
