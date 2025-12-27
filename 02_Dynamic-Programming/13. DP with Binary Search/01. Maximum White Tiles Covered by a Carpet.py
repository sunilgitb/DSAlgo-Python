import bisect
from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        ans = 0
        starts, ends = zip(*tiles)
        dp = [0]*(len(tiles) + 1)
        
        for i in range(len(tiles)):
            dp[i+1] = dp[i] + ends[i] - starts[i] + 1
            
        for l in range(len(tiles)):
            e = starts[l] + carpetLen
            r = bisect.bisect_right(starts, e)
            ans = max(ans, dp[r] - dp[l] - max(0, ends[r-1] - e + 1))
            
        return ans


# Test cases
t1 = [[1,5],[10,11],[12,18],[20,25],[30,32]]
c1 = 10

t2 = [[10,11],[1,1]]
c2 = 2

t3 = [[1,1000000000]]
c3 = 1000000000

solution = Solution()
print("Test 1:", solution.maximumWhiteTiles(t1, c1))  # Expected: 9
print("Test 2:", solution.maximumWhiteTiles(t2, c2))  # Expected: 2
print("Test 3:", solution.maximumWhiteTiles(t3, c3))  # Expected: 1000000000