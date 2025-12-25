# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#

#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def topView(self,root):
        distanceDic = {}
        q = []
        
        if not root: 
            return q
        q.append([root, 0]) # Elements of q is [Node, Horizontal distance of that node from root]
        
        while q:
            tmp = q.pop(0)
            node = tmp[0]
            dis = tmp[1]
            if dis not in distanceDic: 
                distanceDic[dis] = node.data
            if node.left: 
                # Add left child with horizontal distance -1
                q.append([node.left, dis - 1])
            if node.right: 
                # Add right child with horizontal distance +1
                q.append([node.right, dis + 1])
        
        distanceDicKeys = list(distanceDic.keys())
        distanceDicKeys.sort()
        
        ans = []
        for i in distanceDicKeys:
            ans.append(distanceDic[i])
        
        return ans

# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
#        \   \
#         4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
solution = Solution()
print(solution.topView(root))  # Output: [2, 1, 3, 5]

        