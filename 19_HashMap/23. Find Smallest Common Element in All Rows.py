# https://www.lintcode.com/problem/3684/

class Solution:
    def smallest_common_element(self, mat: List[List[int]]) -> int:
        cnt = {}
        for i in range(len(mat)):
            rowset = set()
            for j in range(len(mat[0])):
                if mat[i][j] not in rowset:
                    if mat[i][j] not in cnt: cnt[mat[i][j]] = 1
                    else: cnt[mat[i][j]] += 1
                    rowset.add(mat[i][j])
        
        res = 2**31
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if cnt[mat[i][j]] == len(mat) and mat[i][j] < res:
                    res = mat[i][j]
        
        return res if res != 2**31 else -1

# Time: O(N^2)
if __name__ == "__main__":
    solution = Solution()
    
    mat = [
        [1, 2, 3, 4, 5],
        [2, 4, 5, 8, 10],
        [3, 5, 7, 9, 11],
        [1, 3, 5, 7, 9]
    ]
    print(solution.smallest_common_element(mat))  # Output: 5

    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(solution.smallest_common_element(mat))  # Output: -1
