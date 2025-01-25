from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def longest_common_prefix(self, word: str) -> int:
        node = self.root
        prefix_length = 0

        for char in word:
            if char in node.children:
                prefix_length += 1
                node = node.children[char]
            else:
                break

        return prefix_length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(str(num))

        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.longest_common_prefix(str(num)))

        return max_length
