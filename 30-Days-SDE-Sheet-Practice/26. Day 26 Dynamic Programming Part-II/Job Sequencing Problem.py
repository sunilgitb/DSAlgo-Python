# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
# https://youtu.be/LjPx4wQaRIs

class Solution:
    def JobScheduling(self,Jobs,n):
        jobs = list(Jobs)
        jobs.sort(key = lambda x:x[2], reverse = True)
        arr = [-1] * (n+1)
        
        for job in jobs:
        	d = job[1]
        	p = job[2]
        	if arr[d] == -1:
        		arr[d] = p
        	else:
        		for j in range(d-1, 0, -1):
        			if arr[j] == -1:
        				arr[j] = p
        				break
        
        count = 0
        res = 0
        for i in range(n+1):
        	if arr[i] != -1:
        		count += 1
        		res += arr[i]
        
        
        return(count, res)
        
        
# Time: O(N^2)
# Space: O(N)
# Example Usage:
if __name__ == "__main__":
	Jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
	n = len(Jobs)
	solution = Solution()
	result = solution.JobScheduling(Jobs, n)
	print(result)  # Output: (2, 60)