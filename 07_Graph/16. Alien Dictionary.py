# https://www.geeksforgeeks.org/problems/alien-dictionary/1
# https://www.youtube.com/watch?v=6kTZYvNNyps

class Solution:
    def findOrder(self, alien_dict, N, K):
        
        adj = {char: set() for word in alien_dict for char in word}
    
        for i in range(len(alien_dict) - 1):
            w1, w2 = alien_dict[i], alien_dict[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
    
        visited = {}  # {char: bool} False = visited, True = current path
        res = []
    
        def dfs(char):
            if char in visited:
                return visited[char]
    
            visited[char] = True
    
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
    
            visited[char] = False
            res.append(char)
            return False
    
        for char in adj:
            if dfs(char):
                return ""
    
        res.reverse()
        return "".join(res)


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    alien_dict = ["baa", "abcd", "abca", "cab", "cad"]
    N = 5
    K = 4

    obj = Solution()
    print(obj.findOrder(alien_dict, N, K))
    # Output: bdac
