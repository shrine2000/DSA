class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        indices = [[] for _ in range(256)]
        for i, char in enumerate(word):
            indices[ord(char)].append(i)
        special_count = 0
        
        for i in range(26):
            x = ord('a') + i
            y = ord('A') + i
            if not indices[x]:
                continue
            if not indices[y]:
                continue
            if indices[x][-1] < indices[y][0]:
                special_count += 1
                
        return special_count
            
            
        