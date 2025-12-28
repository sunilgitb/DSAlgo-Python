# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# N Meetings in One Room
# Given start and end times of N meetings, find the maximum number of meetings
# that can be held in a single room (without overlap).

class Solution:
    def maximumMeetings(self, n: int, start: list[int], end: list[int]) -> int:
        """
        :param n: Number of meetings
        :param start: List of start times
        :param end: List of end times
        :return: Maximum number of non-overlapping meetings
        """
        # Step 1: Create list of meetings with index, start, and end times
        meetings = []
        for i in range(n):
            meetings.append([i, start[i], end[i]])
        
        # Step 2: Sort meetings by END time (greedy: pick meeting that ends earliest)
        meetings.sort(key=lambda x: x[2])
        
        # Step 3: Initialize with first meeting
        count = 1
        prev_end = meetings[0][2]
        
        # Step 4: Iterate through remaining meetings
        for i in range(1, n):
            if meetings[i][1] > prev_end:  # start time after previous end time
                count += 1
                prev_end = meetings[i][2]  # update end time
        
        return count


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Example from GFG
        (6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]),  # Expected: 4
        
        # All meetings overlap
        (4, [1, 2, 3, 4], [5, 6, 7, 8]),  # Expected: 1
        
        # No overlap
        (5, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]),  # Expected: 5
        
        # Single meeting
        (1, [10], [20]),  # Expected: 1
        
        # Meetings ending at same time
        (3, [1, 2, 3], [4, 4, 4]),  # Expected: 1
        
        # Another classic case
        (6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]),  # Expected: 4
        
        # Mixed with duplicates
        (4, [0, 1, 1, 2], [3, 4, 2, 5]),  # Expected: 3
    ]
    
    print("Testing N Meetings in One Room\n" + "="*40)
    
    for idx, (n, start, end) in enumerate(test_cases, 1):
        sol = Solution()
        result = sol.maximumMeetings(n, start, end)
        print(f"Test {idx:2d}:")
        print(f"   Start times: {start}")
        print(f"   End times  : {end}")
        print(f"   Max meetings: {result}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()