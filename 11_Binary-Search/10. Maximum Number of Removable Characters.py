# https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(mid):
            remove = set(removable[:mid+1])
            i = j = 0
            while i < len(s) and j < len(p):
                if s[i] == p[j] and i not in remove:
                    j += 1
                i += 1
            return j == len(p)
        
        
        res = 0
        l, r = 0, len(removable)-1
        while l <= r:
            mid = l + (r - l)//2
            if isSubsequence(mid):
                res = max(res, mid+1)
                l = mid + 1
            else:
                r = mid - 1
        
        return res
    
 # Driver code:
if __name__ == "__main__":
    sol = Solution()
    s = "abcacb"
    p = "ab"
    removable = [3,1,0]
    print(sol.maximumRemovals(s, p, removable))  # Output: 2
# Complexity Analysis:
# Time: (n * log(k))   # n = len(s), k = len(removable)
# Space: O(k)
# Binary Search + Two Pointers
# We use binary search to find the maximum number of removable characters.
# For each mid value in binary search, we check if p is still a subsequence of
# s after removing the first mid characters from removable using two pointers.
# If p is still a subsequence, we try to remove more characters by moving the
# left pointer up. Otherwise, we reduce the number of removable characters by
# moving the right pointer down.