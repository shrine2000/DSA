class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        
        queue = [(0, 0)] 
        visited = set()
        distance = 0
        
        while queue:
            next_level = []
            while queue:
                i, j = queue.pop()
                if (i, j) in visited:
                    continue
                while i < len1 and j < len2 and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == len1 and j == len2:
                    return distance
                if (i, j + 1) not in visited:
                    next_level.append((i, j + 1))
                if (i + 1, j) not in visited:
                    next_level.append((i + 1, j))
                if (i + 1, j + 1) not in visited:
                    next_level.append((i + 1, j + 1))
                visited.add((i, j))
            distance += 1
            queue = next_level
