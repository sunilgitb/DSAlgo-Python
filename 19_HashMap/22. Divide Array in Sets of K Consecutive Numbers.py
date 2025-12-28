# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = collections.Counter(nums)
        numset = sorted(list(cnt.keys()))
        i = 0
        while i < len(numset):
            c = numset[i]
            if cnt[c] > 0:
                for j in range(k):
                    cnt[c+j] -= 1
                    if cnt[c+j] < 0: return False
            else:
                i += 1
        
        return True

if __name__ == "__main__":
    solution = Solution()
    
    nums = [1,2,3,3,4,4,5,6]
    k = 4
    print(solution.isPossibleDivide(nums, k))  # Output: True
    # Explanation: Can be divided into [1,2,3,4] and [3,4,5,6]
    
    nums = [3,3,2,2,1,1]
    k = 3
    print(solution.isPossibleDivide(nums, k))  # Output: True
    # Explanation: Can be divided into [1,2,3] and [1,2,3]
    
    nums = [1,2,3,4]
    k = 3
    print(solution.isPossibleDivide(nums, k))  # Output: False
    # Explanation: Cannot divide into sets of 3 consecutive numbers

      

# Time: O(N log(N))
