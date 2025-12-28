# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
# Job Sequencing Problem
# Given N jobs with deadline and profit. Each job takes 1 unit time.
# Find the maximum profit and number of jobs that can be scheduled.

from typing import List, Tuple


class Solution:
    def JobScheduling(self, jobs: List[Tuple[int, int, int]], n: int) -> Tuple[int, int]:
        """
        Greedy Approach (Optimal):
        - Sort jobs by profit in descending order
        - For each job (highest profit first):
          - Try to schedule it as late as possible (within its deadline)
          - Use a set to track booked time slots
        - Time Complexity: O(N log N) for sorting + O(N * max_deadline) for scheduling
        - Space Complexity: O(max_deadline)
        
        Returns: (count of jobs scheduled, total profit)
        """
        # Sort jobs by profit descending
        jobs.sort(key=lambda x: x[2], reverse=True)
        
        # Track booked time slots
        booked = set()
        total_profit = 0
        job_count = 0
        
        for _, deadline, profit in jobs:
            # Try to schedule as late as possible
            slot = deadline
            while slot > 0 and slot in booked:
                slot -= 1
            
            if slot > 0:
                booked.add(slot)
                total_profit += profit
                job_count += 1
        
        return job_count, total_profit


# Driver Code with test cases
def run_tests():
    test_cases = [
        # Example 1
        (4, [(1,4,20), (2,1,10), (3,1,40), (4,1,30)], (2, 60)),
        
        # Example 2
        (5, [(1,2,100), (2,1,19), (3,2,27), (4,1,25), (5,1,15)], (2, 127)),
        
        # All jobs can be done
        (3, [(1,3,10), (2,3,20), (3,3,30)], (3, 60)),
        
        # Tight deadlines
        (4, [(1,1,10), (2,1,20), (3,1,30), (4,1,40)], (1, 40)),
        
        # No jobs
        (0, [], (0, 0)),
    ]
    
    print("Testing Job Sequencing Problem\n" + "="*50)
    
    for idx, (n, jobs, expected) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.JobScheduling(jobs, n)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Jobs: {jobs}")
        print(f"   Output: {result} (Expected: {expected})")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()