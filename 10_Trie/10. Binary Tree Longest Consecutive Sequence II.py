# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class (this is what was missing or not in scope)
class Solution:
    def longestConsecutive2(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_length = 1  # at least 1 (single node)
        
        def postorder(node):
            if not node:
                return [0, 0]  # [inc, dec]
            
            left_inc, left_dec = postorder(node.left)
            right_inc, right_dec = postorder(node.right)
            
            cur_inc = 1
            cur_dec = 1
            
            if node.left:
                if node.left.val == node.val + 1:
                    cur_inc = max(cur_inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    cur_dec = max(cur_dec, left_dec + 1)
            
            if node.right:
                if node.right.val == node.val + 1:
                    cur_inc = max(cur_inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    cur_dec = max(cur_dec, right_dec + 1)
            
            # Longest path through current node: inc + dec - 1 (node counted twice)
            self.max_length = max(self.max_length, cur_inc + cur_dec - 1)
            
            return [cur_inc, cur_dec]
        
        postorder(root)
        return self.max_length

# Helper function to build tree from list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0, 3, None, None, -1]),           # Expected: 3
        ([2, 1, 3]),                               # Expected: 2
        ([1]),                                     # Expected: 1
        ([1, 2, 3, 4, 5]),                         # Expected: 4
        ([5, 4, 6, 3, None, None, 7]),             # Expected: 3
    ]

    for values in test_cases:
        root = build_tree(values)
        sol = Solution()
        result = sol.longestConsecutive2(root)
        print(f"Tree: {values} → Longest consecutive sequence = {result}")