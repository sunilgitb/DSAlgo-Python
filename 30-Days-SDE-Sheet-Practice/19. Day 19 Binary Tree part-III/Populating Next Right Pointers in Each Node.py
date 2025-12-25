# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: 
            return 
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                node.next = q[0] if (q and i < n-1) else None
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        
        return root

# Time: O(N)
# Space: O(N)


if __name__ == "__main__":
    # local Node definition for example (matches LeetCode node)
    class Node:
        def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next

    def print_tree_next_pointers(root):
        """Print nodes level by level showing next pointers as val->next_val (None if no next)."""
        level_start = root
        while level_start:
            curr = level_start
            level_nodes = []
            next_level_start = None
            while curr:
                nxt = curr.next.val if curr.next else None
                level_nodes.append(f"{curr.val}->{nxt}")
                if not next_level_start:
                    next_level_start = curr.left or curr.right
                curr = curr.next
            print("  ".join(level_nodes))
            level_start = next_level_start

    # Example tree (perfect binary tree of depth 3):
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4  5  6   7
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    sol = Solution()
    sol.connect(n1)
    print("Next pointers by level:")
    print_tree_next_pointers(n1)