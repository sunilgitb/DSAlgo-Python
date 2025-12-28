# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        def dfs(node):
            if node in safe:        # Cycle found or previously checked
                return safe[node]
            safe[node] = False      # NOTE: FOR CYCLE DETECTION
            for i in graph[node]:
                if not dfs(i):      # visited i and not safe
                    return safe[i]  # stop further check
            safe[node] = True       # all outgoing edges had been checked so safe node
            return safe[node]
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res

'''
NOTE:  
initializing safe[node] = False, so before traversing all outgoing edges 
if we again reach node i.e, loop detected then return safe[node].
'''


# Time: O(N)
if __name__ == "__main__":
    solution = Solution()
    
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    # Explanation: Nodes 5 and 6 are terminal nodes. Safe nodes are those that eventually lead to terminal nodes.
    print(solution.eventualSafeNodes(graph))  # Output: [2,4,5,6]

    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(solution.eventualSafeNodes(graph))  # Output: [4]
