# https://leetcode.com/problems/score-after-flipping-matrix/description/

# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Step 1: Ensure first column is all 1s by flipping rows if needed
        for i in range(rows):
            if grid[i][0] == 0:
                grid[i] = [1 - x for x in grid[i]]
        
        # Step 2: For each column (except first), flip if zeros are more than ones
        for j in range(1, cols):
            ones = sum(grid[i][j] for i in range(rows))
            if ones < rows / 2:
                for i in range(rows):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 3: Calculate the total score
        res = 0
        for row in grid:
            num = 0
            for j in range(cols):
                num += row[j] << (cols - j - 1)  # faster than 2**(cols-j-1)
            res += num
        
        return res


# -------- Driver Code --------
solution = Solution()

grid1 = [[0,0,1,1],
         [1,0,1,0],
         [1,1,0,0]]
print(solution.matrixScore(grid1))  # Output: 39

grid2 = [[0]]
print(solution.matrixScore(grid2))  # Output: 1
