# https://leetcode.com/problems/get-equal-substrings-within-budget/
'''
Calculate the differences between a[i] and b[i].
Use a sliding window to track the longest valid substring.
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Calculate cost differences
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        
        curCost = 0
        res = 0
        l = 0
        
        # Sliding window
        for r in range(len(costs)):
            curCost += costs[r]
            
            while curCost > maxCost:
                curCost -= costs[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print(solution.equalSubstring(s, t, maxCost))  
    # Output: 3
    # Explanation: substring "abc" -> "bcd" costs [1,1,1] = 3
    
    s = "abcd"
    t = "cdef"
    maxCost = 3
    print(solution.equalSubstring(s, t, maxCost))  
    # Output: 1
    
    s = "abcd"
    t = "acde"
    maxCost = 0
    print(solution.equalSubstring(s, t, maxCost))  
    # Output: 1

    
    
# Time: O(N)
