# https://leetcode.com/problems/minimum-window-substring/

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last occurrence of each character
        lastIndex = {ch: i for i, ch in enumerate(s)}
        res = []
        left = -1
        right = 0
        
        for i, ch in enumerate(s):
            # Extend the right boundary of current partition
            right = max(right, lastIndex[ch])
            
            # If we reach the end of the current partition
            if i == right:
                res.append(right - left)
                left = i  # move left to the end of this partition
                
        return res


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s))  # Output: [9, 7, 8]

    # Test Case 2
    s = "eccbbbbdec"
    print(solution.partitionLabels(s))  # Output: [10]

    # Test Case 3
    s = "caedbdedda"
    print(solution.partitionLabels(s))  # Output: [1, 9]
