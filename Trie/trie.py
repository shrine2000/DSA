from typing import List
from collections import deque


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word: str = ""


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def search_prefix(self, prefix: str) -> str:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
            if node.is_end_of_word:
                return node.word
        return None

    @staticmethod
    def replaceWords(dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        def replace(word: str) -> str:
            for i in range(len(word)):
                prefix = word[: i + 1]
                root = trie.search_prefix(prefix)
                if root:
                    return root
            return word

        replace_sentence: List[str] = [replace(word) for word in sentence.split()]
        return " ".join(replace_sentence)

    @staticmethod
    def longestWord(words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        longest_word = ""
        queue = deque([(trie.root, "")])
        while queue:
            node, current_word = queue.popleft()
            if node.is_end_of_word:
                if len(current_word) > len(longest_word):
                    longest_word = current_word
            for char, child_node in node.children.items():
                queue.append((child_node, current_word + char))

        return longest_word


if __name__ == "__main__":
    # Test cases
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    replaced_sentence = Trie.replaceWords(dictionary, sentence)
    print(replaced_sentence)  # Output: "the cat was rat by the bat"

    # Test Trie functionality
    trie = Trie()
    words_to_insert = ["apple", "banana", "orange", "app", "ban"]
    for word in words_to_insert:
        trie.insert(word)

    assert trie.search("apple") == True
    assert trie.search("banana") == True
    assert trie.search("orange") == True
    assert trie.search("app") == True
    assert trie.search("ban") == True
    assert trie.search("grape") == False

    assert trie.startsWith("app") == True
    assert trie.startsWith("or") == True
    assert trie.startsWith("gr") == False

    # Test longestWord method
    words = ["w", "wo", "wor", "worl", "world", "word", "abc"]
    print(Trie.longestWord(words))  # Output: "world"
