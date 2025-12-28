# https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

class Solution:
    def toh(self, n, from_rod, to_rod, aux_rod):
        if n == 0: 
            return 0
        moves = 0
        moves += self.toh(n-1, from_rod, aux_rod, to_rod)
        print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
        moves += 1
        moves += self.toh(n-1, aux_rod, to_rod, from_rod)
        return moves


# ---------------- Driver Code ----------------

if __name__ == "__main__":
    n = 3
    solution = Solution()
    total_moves = solution.toh(n, 'A', 'C', 'B')
    print("Total moves:", total_moves)

"""
Expected Output:
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
Total moves: 7
"""
