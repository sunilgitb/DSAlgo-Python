# https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

import collections

class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        q = collections.deque()
        
        # Convert to 0-based indexing
        start_x, start_y = KnightPos[0] - 1, KnightPos[1] - 1
        target_x, target_y = TargetPos[0] - 1, TargetPos[1] - 1
        
        q.append((start_x, start_y, 0))
        
        visited = [[False] * N for _ in range(N)]
        visited[start_x][start_y] = True
        
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        while q:
            i, j, steps = q.popleft()
            
            if i == target_x and j == target_y:
                return steps
            
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                    visited[x][y] = True
                    q.append((x, y, steps + 1))
        
        return -1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    N = 8
    KnightPos = [1, 1]
    TargetPos = [8, 8]

    sol = Solution()
    print(sol.minStepToReachTarget(KnightPos, TargetPos, N))
