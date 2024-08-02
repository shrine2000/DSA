from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
    def add_word(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = TrieNode()
        for word in words:
            trie.add_word(word)
            
        r, c = len(board), len(board[0])   
        res, visited = set(), set()
        
        def dfs(i, j, node, word):
            if not (0 <= i < r and 0 <= j < c and (i, j) not in visited and board[i][j] in node.children):
                return
            visited.add((i, j))
            
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.is_end:
                res.add(word)
                node.is_end = False
            
            dfs(i + 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j - 1, node, word)
            
            visited.remove((i, j))      
            
        for i in range(r):
            for j in range(c):
                if board[i][j] in trie.children:
                    dfs(i, j, trie, "")
                
        return list(res)
