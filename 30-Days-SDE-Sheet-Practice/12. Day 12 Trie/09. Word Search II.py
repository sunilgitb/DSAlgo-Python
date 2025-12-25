# https://leetcode.com/problems/word-search-ii/
# https://youtu.be/asbcE9mZz_U
'''
In Brute Force DFS time complexity: O(k * m * n * 4^(m*n)) where k = len(words)
But we can remove the k if we store all the words into a TRIE.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        row = len(board);
        col = len(board[0])
        res = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= row or c >= col or 
                board[r][c] not in node.children or board[r][c] == '#'):
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
                node.endOfWord = False
            tmp = board[r][c]
            board[r][c] = '#'
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            board[r][c] = tmp
            
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        
        return res
    
# Time: O(m * n * 4^(m*n))
# Space: O(m*n + k)


if __name__ == '__main__':
    # Driver code 🔧
    sol = Solution()

    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    expected1 = {"oath","eat"}
    ans1 = sol.findWords(board1, words1)
    print(f"findWords(board1, {words1}) => {ans1} (expected {expected1})")
    assert ans1 == expected1, f"Test1 failed: got {ans1}"

    board2 = [["a"]]
    words2 = ["a"]
    expected2 = {"a"}
    ans2 = sol.findWords(board2, words2)
    print(f"findWords(board2, {words2}) => {ans2} (expected {expected2})")
    assert ans2 == expected2, f"Test2 failed: got {ans2}"

    print('All tests passed ✅')
