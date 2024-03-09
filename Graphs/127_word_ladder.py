from collections import deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        word, transformations = queue.popleft()
        if word == endWord:
            return transformations

        for pos in range(len(word)):
            for ind in range(26):
                alphabet = chr(ord("a") + ind)
                new_word = word[:pos] + alphabet + word[pos + 1 :]
                if new_word in wordSet:
                    queue.append((new_word, transformations + 1))
                    wordSet.remove(new_word)
    return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))
