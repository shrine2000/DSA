from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        adj_list = defaultdict(list)
        
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current, level = queue.popleft()
            
            for i in range(len(current)):
                pattern = current[:i] + '*' + current[i+1:]
                for neighbor in adj_list[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                adj_list[pattern] = []
                
        return 0
