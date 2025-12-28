# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {ch:i for i, ch in enumerate(s)}
        res = []
        left = -1
        right = 0
        
        for i, ch in enumerate(s):
            right = max(right, lastIndex[ch])
            if i == right:
                res.append(right - left)
                right = i
                left = i
        
        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    s = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s))  # Output: [9, 7, 8]

    s = "eccbbbbdec"
    print(solution.partitionLabels(s))  # Output: [10]

    s = "caedbdedda"
    print(solution.partitionLabels(s))  # Output: [1, 9]

# Time: O(N)
# Space: O(N)
