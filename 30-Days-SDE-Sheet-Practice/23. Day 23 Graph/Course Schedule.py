# https://leetcode.com/problems/course-schedule/
# This problem if a variation of Topological Sort
 
# DFS
from typing import List
import collections

# ---------------- DFS SOLUTION ----------------
class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        completed = set()
        visited = set()

        def canTake(course):
            if course in completed:
                return True
            if course in visited:
                return False  # cycle detected

            visited.add(course)
            for c in adjList[course]:
                if not canTake(c):
                    return False

            visited.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not canTake(course):
                return False

        return True


# ---------------- BFS SOLUTION ----------------
class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        outbound = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            outbound[prereq] += 1

        q = collections.deque()
        for course in outbound:
            if outbound[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            for c in adjList[course]:
                outbound[c] -= 1
                if outbound[c] == 0:
                    q.append(c)

        for course in outbound:
            if outbound[course] != 0:
                return False

        return True


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    dfs = SolutionDFS()
    bfs = SolutionBFS()

    test_cases = [
        (2, [[1, 0]]),                 # True
        (2, [[1, 0], [0, 1]]),         # False (cycle)
        (4, [[1,0],[2,1],[3,2]]),      # True
        (3, [[0,1],[1,2],[2,0]])       # False (cycle)
    ]

    for i, (numCourses, prerequisites) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("DFS Result:", dfs.canFinish(numCourses, prerequisites))
        print("BFS Result:", bfs.canFinish(numCourses, prerequisites))

# Time for both dfs and bfs is = number of nodes + number of edges
# n = numCourses; e = len(prerequisites)
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)
