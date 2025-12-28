# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        rows, cols = len(board), len(board[0])
        res = set()

        for word in words:
            root.addWord(word)

        def dfs(r, c, node, path):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "#" or
                board[r][c] not in node.children
            ):
                return

            ch = board[r][c]
            node = node.children[ch]
            path += ch

            if node.isWord:
                res.add(path)
                node.isWord = False  # avoid duplicates

            board[r][c] = "#"
            dfs(r + 1, c, node, path)
            dfs(r - 1, c, node, path)
            dfs(r, c + 1, node, path)
            dfs(r, c - 1, node, path)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)


# ---------------- DRIVER CODE ----------------

board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]

words = ["oath","pea","eat","rain"]

sol = Solution()
print(sol.findWords(board, words))
