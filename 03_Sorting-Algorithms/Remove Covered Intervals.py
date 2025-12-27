from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = right = 0
        for l, r in intervals:
            res += r > right
            right = max(r, right)
        return res

    def removeCoveredIntervals_stack(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        stack = []
        cnt = 0
        for l, r in intervals:
            while stack and l <= stack[-1][0] and stack[-1][1] <= r:
                stack.pop()
                cnt += 1
            stack.append((l, r))
        
        return len(intervals) - cnt


# Test cases
solution = Solution()

# Test 1
intervals1 = [[1,4],[3,6],[2,8]]
print("Test 1 (method 1):", solution.removeCoveredIntervals(intervals1))  # Expected: 2
print("Test 1 (method 2):", solution.removeCoveredIntervals_stack(intervals1))  # Expected: 2

# Test 2
intervals2 = [[1,4],[2,3]]
print("\nTest 2 (method 1):", solution.removeCoveredIntervals(intervals2))  # Expected: 1
print("Test 2 (method 2):", solution.removeCoveredIntervals_stack(intervals2))  # Expected: 1

# Test 3
intervals3 = [[0,10],[5,12]]
print("\nTest 3 (method 1):", solution.removeCoveredIntervals(intervals3))  # Expected: 2
print("Test 3 (method 2):", solution.removeCoveredIntervals_stack(intervals3))  # Expected: 2

# Test 4
intervals4 = [[3,10],[4,10],[5,11]]
print("\nTest 4 (method 1):", solution.removeCoveredIntervals(intervals4))  # Expected: 2
print("Test 4 (method 2):", solution.removeCoveredIntervals_stack(intervals4))  # Expected: 2

# Test 5
intervals5 = [[1,2],[1,4],[3,4]]
print("\nTest 5 (method 1):", solution.removeCoveredIntervals(intervals5))  # Expected: 1
print("Test 5 (method 2):", solution.removeCoveredIntervals_stack(intervals5))  # Expected: 1

# Test 6
intervals6 = [[1,5],[2,6],[3,4]]
print("\nTest 6 (method 1):", solution.removeCoveredIntervals(intervals6))  # Expected: 3
print("Test 6 (method 2):", solution.removeCoveredIntervals_stack(intervals6))  # Expected: 3

# Verify both methods give same results
print("\n" + "="*50)
print("Verification that both methods give same results:")
test_intervals = [intervals1, intervals2, intervals3, intervals4, intervals5, intervals6]
all_match = True
for i, intervals in enumerate(test_intervals, 1):
    method1 = solution.removeCoveredIntervals(intervals)
    method2 = solution.removeCoveredIntervals_stack(intervals)
    if method1 == method2:
        print(f"Test {i}: ✓ Both methods return {method1}")
    else:
        print(f"Test {i}: ✗ Methods differ: {method1} vs {method2}")
        all_match = False

if all_match:
    print("\nAll tests passed! Both methods give identical results.")