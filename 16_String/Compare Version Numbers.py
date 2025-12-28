# https://leetcode.com/problems/compare-version-numbers/
''' 
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        i = 0
        j = 0
        while i < len(v1) or j < len(v2):
            n1 = 0
            k = i
            if k < len(v1):
                while k < len(v1) and v1[k] != '.':
                    k += 1
                n1 = int(v1[i:k])
            i = k + 1
            
            n2 = 0
            k = j 
            if k < len(v2):
                while k < len(v2) and v2[k] != '.':
                    k += 1
                n2 = int(v2[j:k])
            j = k + 1
            
            if n1 < n2: return -1
            if n1 > n2: return 1
        
        return 0

# Time: O(N^2)
# Space: O(1)
'''


import collections

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = collections.deque(version1.split("."))
        v2 = collections.deque(version2.split("."))
        
        while v1 or v2:
            v1_val = int(v1.popleft()) if v1 else 0
            v2_val = int(v2.popleft()) if v2 else 0
            
            if v1_val > v2_val:
                return 1
            if v1_val < v2_val:
                return -1
        
        return 0


# -------- Driver Code --------
solution = Solution()

print(solution.compareVersion("1.01", "1.001"))   # 0
print(solution.compareVersion("1.0", "1.0.0"))    # 0
print(solution.compareVersion("0.1", "1.1"))      # -1
print(solution.compareVersion("1.2", "1.10"))     # -1
print(solution.compareVersion("3.5.2", "3.5.1"))  # 1

    
# Time: O(N)  ; as pop from deque is constant time
# Space: O(N) ; for making v1 and v2


