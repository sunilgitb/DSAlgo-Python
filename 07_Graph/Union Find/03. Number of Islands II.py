from typing import List
from collections import defaultdict

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class UnionFind:
    def __init__(self, num):
        self.root = [-1] * num  # -1 means water/not initialized
        self.rank = [0] * num
        self.size = num
    
    def initialize(self, idx):
        """Initialize a cell as land (its own parent)"""
        if self.root[idx] == -1:
            self.root[idx] = idx
    
    def find(self, u):
        """Find with path compression"""
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        """Union by rank, returns True if union happened"""
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False  # Already connected
        
        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.root[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.root[root_v] = root_u
        else:
            self.root[root_v] = root_u
            self.rank[root_u] += 1
        
        return True  # Successfully merged

class Solution:
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        """
        n: number of rows
        m: number of columns
        operators: list of points to convert to land
        
        Returns: List of island counts after each operation
        """
        if not operators:
            return []
        
        # Directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        uf = UnionFind(n * m)
        count = 0  # Current number of islands
        
        def get_index(i, j):
            """Convert 2D coordinates to 1D index"""
            return i * m + j
        
        print(f"Grid: {n} x {m}")
        print(f"Total operations: {len(operators)}")
        print("=" * 60)
        
        for idx, point in enumerate(operators):
            i, j = point.x, point.y
            print(f"\nOperation {idx + 1}: Add land at ({i}, {j})")
            
            # Check if this cell is already land
            current_index = get_index(i, j)
            if uf.root[current_index] != -1:
                print(f"  Cell ({i}, {j}) is already land")
                result.append(count)
                continue
            
            # Convert water to land
            print(f"  Converting water to land at index {current_index}")
            uf.initialize(current_index)
            count += 1  # Start by assuming it's a new island
            print(f"  Initial: count = {count} (assume new island)")
            
            # Check 4 neighbors
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    neighbor_index = get_index(x, y)
                    
                    # Check if neighbor is land
                    if uf.root[neighbor_index] != -1:
                        print(f"  Neighbor ({x}, {y}) at index {neighbor_index} is land")
                        print(f"    Root of current: {uf.find(current_index)}")
                        print(f"    Root of neighbor: {uf.find(neighbor_index)}")
                        
                        # If they're not already connected, union them
                        if uf.union(current_index, neighbor_index):
                            count -= 1  # Merged two islands
                            print(f"    ✓ Merged! Count decreased to {count}")
                        else:
                            print(f"    ✗ Already connected")
            
            result.append(count)
            
            # Visualization
            print(f"\n  Current grid state:")
            self.print_grid(n, m, uf)
            print(f"  Total islands: {count}")
        
        return result
    
    def print_grid(self, n, m, uf):
        """Print current grid state"""
        for i in range(n):
            row = []
            for j in range(m):
                idx = i * m + j
                if uf.root[idx] == -1:
                    row.append("W")  # Water
                else:
                    row.append("L")  # Land
            print("    " + " ".join(row))


# Test the solution
def run_example():
    print("=" * 60)
    print("NUMBER OF ISLANDS II - UNION FIND SOLUTION")
    print("=" * 60)
    
    solution = Solution()
    
    # Example 1
    print("\nExample 1: 3x3 grid")
    n, m = 3, 3
    operators = [
        Point(0, 0), Point(0, 1), Point(1, 2),
        Point(2, 1), Point(1, 1), Point(2, 2)
    ]
    
    print("Operations sequence:")
    for i, op in enumerate(operators):
        print(f"  {i+1}. ({op.x}, {op.y})")
    
    result = solution.num_islands2(n, m, operators)
    print(f"\nResult: {result}")
    
    # Example 2: More complex
    print("\n" + "=" * 60)
    print("\nExample 2: 4x5 grid")
    n, m = 4, 5
    operators = [
        Point(1, 1), Point(0, 1), Point(3, 3),
        Point(3, 4), Point(2, 4), Point(2, 3),
        Point(1, 3), Point(0, 3), Point(1, 2),
        Point(2, 2)
    ]
    
    result = solution.num_islands2(n, m, operators)
    print(f"\nResult: {result}")
    print("=" * 60)


if __name__ == "__main__":
    run_example()