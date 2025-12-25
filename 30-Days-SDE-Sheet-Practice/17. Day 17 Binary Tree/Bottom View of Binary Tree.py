# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1#

import collections

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        distDict = {}
        
        q = collections.deque([(root, 0)])
        while q:
            tmp = q.popleft()
            node = tmp[0]
            dist = tmp[1]
            
            distDict[dist] = node.data
            
            if node.left: 
                q.append((node.left, dist-1))
            if node.right: 
                q.append((node.right, dist+1))
        
        keys = distDict.keys()
        mini = min(keys)
        maxi = max(keys)
        
        res = []
        for key in range(mini, maxi+1):
            if key in distDict:
                res.append(distDict[key])
        
        return res
        
# Time: O(N)
# Space: O(N)

# Example Usage:
if __name__ == "__main__":
    # Constructing the binary tree
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    solution = Solution()
    print(solution.bottomView(root))  # Output: [5, 10, 3, 14, 25]


