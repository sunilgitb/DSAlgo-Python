# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        s = sum(wall[0])
        dct = {0:n, n:n}
        
        for w in wall:
            i = 0
            for j in w[:-1]:
                i += j
                if i not in dct: dct[i] = n-1
                else: dct[i] -= 1
                    
        # print(dct)
        return min(list(dct.values()))

# Driver code
if __name__ == "__main__":
    sol = Solution()
    
    wall1 = [[1,2,2,1],
             [3,1,2],
             [1,3,2],
             [2,4],
             [3,1,2],
             [1,3,1,1]]
             
    wall2 = [[1],[1],[1]]  # all single bricks
    
    wall3 = [[1,1,1,1],
             [2,2],
             [4]]
    
    print("Least bricks to cross wall1:", sol.leastBricks(wall1))  # Expected: 2
    print("Least bricks to cross wall2:", sol.leastBricks(wall2))  # Expected: 3
    print("Least bricks to cross wall3:", sol.leastBricks(wall3))  # Expected: 1
