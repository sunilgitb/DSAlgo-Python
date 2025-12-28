class Solution:
    def findMedian(self, matrix):
        """
        Find the median of a row-wise sorted matrix without extra space.
        Time: O(32 * n * log(m)) ≈ O(n * log(m) * log(max_val))
        Space: O(1)
        """
        if not matrix or not matrix[0]:
            return 0  # or raise error

        n = len(matrix)
        m = len(matrix[0])
        
        # Find global min and max
        low = float('inf')
        high = float('-inf')
        for row in matrix:
            low = min(low, row[0])
            high = max(high, row[-1])

        # Median is at position (n*m + 1) // 2 in 1-based indexing
        # We need the smallest number that has at least (n*m + 1)//2 elements <= it
        target_count = (n * m + 1) // 2

        def count_less_or_equal(mid):
            """Count how many elements <= mid in the entire matrix"""
            count = 0
            for row in matrix:
                # Find the rightmost index where row[i] <= mid
                l, r = 0, m - 1
                while l <= r:
                    md = l + (r - l) // 2
                    if row[md] <= mid:
                        l = md + 1
                    else:
                        r = md - 1
                count += l  # l is the number of elements <= mid in this row
            return count

        while low <= high:
            mid = low + (high - low) // 2
            
            if count_less_or_equal(mid) >= target_count:
                # mid is a candidate → try smaller
                high = mid - 1
            else:
                # Need more elements → go higher
                low = mid + 1

        return low

# Example usage:
matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]
solution = Solution()
print(solution.findMedian(matrix))  # Output: 5