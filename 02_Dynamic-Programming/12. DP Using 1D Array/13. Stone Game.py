from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            # Even turn → Alice's move (maximize)
            if (r - l) % 2 == 0:
                pick_left = piles[l] + dfs(l+1, r)
                pick_right = piles[r] + dfs(l, r-1)
            # Odd turn → Bob's move (minimize Alice's score)
            else:
                pick_left = dfs(l+1, r)
                pick_right = dfs(l, r-1)
            
            memo[(l, r)] = max(pick_left, pick_right)
            return memo[(l, r)]
        
        total_stones = sum(piles)
        return dfs(0, n-1) > total_stones // 2

# ---------------------- Driver Code ----------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    piles1 = [5,3,4,5]
    print(f"Piles: {piles1} -> Alice wins? {solution.stoneGame(piles1)}")  # Expected: True
    
    # Example 2
    piles2 = [3,7,2,3]
    print(f"Piles: {piles2} -> Alice wins? {solution.stoneGame(piles2)}")  # Expected: True
    
    # Example 3
    piles3 = [1,100,2,99]
    print(f"Piles: {piles3} -> Alice wins? {solution.stoneGame(piles3)}")  # Expected: True
