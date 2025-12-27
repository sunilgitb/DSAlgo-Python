import bisect
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        S = [job[0] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        
        for k in range(n-1, -1, -1):
            next_job = bisect.bisect_left(S, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[next_job], dp[k+1])
        
        return dp[0]


# Test cases
solution = Solution()

# Test 1
start1 = [1,2,3,3]
end1 = [3,4,5,6]
profit1 = [50,10,40,70]
print("Test 1:", solution.jobScheduling(start1, end1, profit1))  # Expected: 120

# Test 2
start2 = [1,2,3,4,6]
end2 = [3,5,10,6,9]
profit2 = [20,20,100,70,60]
print("Test 2:", solution.jobScheduling(start2, end2, profit2))  # Expected: 150

# Test 3
start3 = [1,1,1]
end3 = [2,3,4]
profit3 = [5,6,4]
print("Test 3:", solution.jobScheduling(start3, end3, profit3))  # Expected: 6