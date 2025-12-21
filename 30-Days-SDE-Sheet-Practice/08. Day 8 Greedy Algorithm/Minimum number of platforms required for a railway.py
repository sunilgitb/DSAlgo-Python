# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
'''
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
'''

# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
'''
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
'''

class Solution:    
    # Function to find the minimum number of platforms required
    def minimumPlatform(self, n, arr, dep):
        arr.sort()
        dep.sort()
        
        i = 1   # pointer for arrival
        j = 0   # pointer for departure
        
        platformNeeded = 1
        res = 1
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platformNeeded += 1
                i += 1
            else:
                platformNeeded -= 1
                j += 1
            
            res = max(res, platformNeeded)
        
        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(arr)

    print(sol.minimumPlatform(n, arr, dep))
    # Expected Output: 3


# Time: O(N log(N))
# Space: O(N)
        