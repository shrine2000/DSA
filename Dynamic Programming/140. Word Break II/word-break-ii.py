from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_from(self, s, idx):
        node = self.root
        result = []
        for i in range(idx, len(s)):
            char = s[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end:
                result.append(i + 1)
        return result


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if dp[i]:
                word_end_pos = trie.search_from(s, i)
                for end in word_end_pos:
                    dp[end] = True
        return dp[n]
