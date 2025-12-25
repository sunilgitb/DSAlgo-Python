# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
''' 
We keep a track of elements and check for all 4 directions
'''

from typing import List

class Solution:
    def findPath(self, m, n):
        if m[0][0] == 0 or m[-1][-1] == 0: return []
        res = []
        vis = [[False]*n for i in range(n)] # to keep track of visited cells

        def solve(r, c, path):
            if r == n-1 and c == n-1 and m[r][c] == 1:
                res.append(path)
                return
            # Up
            if r-1 >= 0 and m[r-1][c] == 1 and vis[r-1][c] == False:
                vis[r][c] = True
                solve(r-1, c, path + 'U')
                vis[r][c] = False
            # Down
            if r+1 < n and m[r+1][c] == 1 and vis[r+1][c] == False:
                vis[r][c] = True
                solve(r+1, c, path + 'D')
                vis[r][c] = False
            # Left
            if c-1 >= 0 and m[r][c-1] == 1 and vis[r][c-1] == False:
                vis[r][c] = True
                solve(r, c-1, path + 'L')
                vis[r][c] = False
            # Right
            if c+1 < n and m[r][c+1] == 1 and vis[r][c+1] == False:
                vis[r][c] = True
                solve(r, c+1, path + 'R')
                vis[r][c] = False
            
        solve(0, 0, '')
        return sorted(res)
        
# Time: O(N*N)
# Space: O(N*N)
         

if __name__ == '__main__':
    sol = Solution()

    tests = [
        (
            [[1,0,0,0],
             [1,1,0,1],
             [1,1,0,0],
             [0,1,1,1]],
            4,
            'Example 4x4'
        ),
        (
            [[0,1],[1,0]],
            2,
            'Start blocked'
        ),
        (
            [[1]],
            1,
            '1x1 grid'
        ),
        (
            [[1,0],[1,1]],
            2,
            'Simple 2x2'
        )
    ]

    for i, (m, n, desc) in enumerate(tests, 1):
        paths = sol.findPath(m, n)
        print(f"\nTest {i}: {desc} (n={n}) -> {len(paths)} path(s)")
        for p in paths:
            print(p)
        if not paths:
            print('No path found')
