# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        lst = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dpEndTime = [0]
        dpProfit = [0]
        
        for start, end, profit in lst:
            # find rightMost idx to insert this start time
            # idx is where this new start needs to be inserted
            # idx - 1 is the one that doesn't overlap
            idx = self.bSearch(dpEndTime, start)
            lastProfit = dpProfit[-1]
            currProfit = dpProfit[idx-1] + profit # they don't overlap
            
            # whener we find currProfit greater than last, we update
            if currProfit > lastProfit:
                dpEndTime.append(end)
                dpProfit.append(currProfit)
        
        return dpProfit[-1]
            
    
    def bSearch(self, arr, target):  # right most element whose endTime <= current start time. 
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
    
    
# Time: O(N * log(N))
# Space: O(N)
# N = number of jobs
# Sort the jobs based on end time.
# For each job, use binary search to find the last non-overlapping job.
# Use dynamic programming to keep track of maximum profit at each step.
# Example Usage:
sol = Solution()
print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))  # Output: 120