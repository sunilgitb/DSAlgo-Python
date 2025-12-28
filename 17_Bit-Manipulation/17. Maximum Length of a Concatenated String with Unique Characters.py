# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
In this we will store each unique lenght substring separetly and will compare with all the possible permutation.
'''


#----------------------- Method 1 -----------------------
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List

# ---------------- Method 1 ----------------
class Solution1:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): 
                continue
            a_set = set(a)
            for c in dp[:]:
                if a_set & c: 
                    continue
                dp.append(a_set | c)
        return max(len(a) for a in dp)


# ---------------- Method 2 ----------------
class Solution2:
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']
        for a in arr:
            for b in unique[:]:
                if len(a+b) == len(set(a+b)):
                    unique.append(a+b)
        return max(len(a) for a in unique)


# ---------------- Method 3 (DFS) ----------------
class Solution3:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        def dfs(i, s):
            if len(set(s)) < len(s):
                return
            self.res = max(self.res, len(s))
            for j in range(i, len(arr)):
                dfs(j+1, s + arr[j])
        dfs(0, "")
        return self.res


# -------- Driver Code --------
arr = ["un","iq","ue"]

solution1 = Solution1()
solution2 = Solution2()
solution3 = Solution3()

print(solution1.maxLength(arr))  # 4
print(solution2.maxLength(arr))  # 4
print(solution3.maxLength(arr))  # 4

arr2 = ["cha","r","act","ers"]
print(solution1.maxLength(arr2)) # 6
print(solution2.maxLength(arr2)) # 6
print(solution3.maxLength(arr2)) # 6

        
# Time: O(N^2)  # For All Methods 1, 2, 3
