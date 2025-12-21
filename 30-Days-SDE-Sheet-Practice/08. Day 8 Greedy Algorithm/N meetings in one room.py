# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
''' 
We can start a new meeting after its previous meeting ends. So I will 
sort the meeting array based on ending time. So that meetings with low ending time comes fist
'''
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
'''
We can start a new meeting after the previous one ends.
So we sort meetings by their end time (Greedy approach).
'''

class Solution:
    # Function to find the maximum number of meetings
    def maximumMeetings(self, n, start, end):
        # Pair start and end times
        meetings = [[start[i], end[i]] for i in range(n)]
        
        # Sort by ending time
        meetings.sort(key=lambda x: x[1])
        
        count = 1
        lastEnd = meetings[0][1]
        
        for i in range(1, n):
            if meetings[i][0] > lastEnd:
                count += 1
                lastEnd = meetings[i][1]
        
        return count


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()       

    start = [1, 3, 0, 5, 8, 5]
    end   = [2, 4, 6, 7, 9, 9]
    n = len(start)

    print(sol.maximumMeetings(n, start, end))
    # Expected Output: 4

        


class Solution:
    def maximumMeetings(self,n,start,end):
        # code here
        time = [[start[i], end[i]] for i in range(len(start))]
        time.sort(key = lambda x : x[1])
        res = 1
        r = 1
        l = 0
        while r < len(time):
            if time[r][0] > time[l][1]:
                res += 1
                l = r
            r += 1
        
        return res

# Time Complexity : O(N*LogN)
# Auxilliary Space : O(N)