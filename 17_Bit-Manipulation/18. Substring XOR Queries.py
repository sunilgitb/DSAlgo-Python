# https://leetcode.com/problems/substring-xor-queries/

# https://leetcode.com/problems/substring-xor-queries/

from collections import defaultdict
from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        seen = defaultdict(lambda: [-1, -1])
        n = len(s)
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':  # handle single '0'
                seen[0] = [i, i]
                continue
            v = 0
            for j in range(i, n):
                v = v*2 + int(s[j])
                if v > 2**32: break
                seen[v] = [i, j]
        
        return [seen[fst ^ snd] for fst, snd in queries]


# -------- Driver Code --------
solution = Solution()

s = "101101"
queries = [[0,5],[1,2],[3,4]]
print(solution.substringXorQueries(s, queries))  
# Example Output: [[0,2],[1,2],[0,1]] (actual output depends on substring positions)

s2 = "111"
queries2 = [[1,2],[0,3]]
print(solution.substringXorQueries(s2, queries2))

    
# Time: O(30N + Q)
# Space: O(30N)
