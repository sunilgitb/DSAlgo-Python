# https://leetcode.com/problems/clone-graph/


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        curNewDict = {}   # key = curNode; value = copy of curNode
        
        def traverse(curNode):
            if not curNode: return
            if curNode not in curNewDict:
                curNewDict[curNode] = Node(curNode.val)
            for nei in curNode.neighbors:
                if nei and nei not in curNewDict: 
                    curNewDict[nei] = Node(nei.val)
                    traverse(nei)  # only calling if nei is not in dictionary. Here we using the curNewDic to track visited nodes also! 
                curNewDict[curNode].neighbors.append(curNewDict[nei])
                
        traverse(node)
        # return copy of the starting node
        return curNewDict[node]

# Build graph:
# 1 -- 2
# |    |
# 4 -- 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned = solution.cloneGraph(node1)

print(cloned.val)                         # 1
print([n.val for n in cloned.neighbors])  # [2, 4]


# BFS
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        curNewDict = {}   # key = curNode; value = copy of curNode
        
        q = collections.deque()
        q.append(node)
        while q:
            curNode = q.popleft()
            if curNode not in curNewDict: curNewDict[curNode] = Node(curNode.val)
            for nei in curNode.neighbors:
                if nei and nei not in curNewDict: 
                    curNewDict[nei] = Node(nei.val)
                    q.append(nei)  # we are not using any visited set to avoid loop. As we are only appending nei, if nei is not in dictionary. Here we using the curNewDic to track visited nodes also! 
                curNewDict[curNode].neighbors.append(curNewDict[nei])
        # return copy of the starting node
        return curNewDict[node]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned = solution.cloneGraph(node1)

print(cloned.val)                         # 1
print([n.val for n in cloned.neighbors])  # [2, 4]



# Time for both dfs and bfs is = number of nodes + number of edges
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)