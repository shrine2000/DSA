class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1
        for index, char in enumerate(s):
            if counter[char] == 1:
                return index
        return -1