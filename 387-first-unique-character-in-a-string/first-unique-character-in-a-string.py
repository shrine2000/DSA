class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for k, v in counter.items():
            if v == 1:
                return s.index(k)  
        return -1