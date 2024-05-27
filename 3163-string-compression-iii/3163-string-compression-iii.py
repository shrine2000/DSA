class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            c = word[0]
            count = 0
            while count < len(word) and count < 9 and word[count] == c:
                count += 1
            comp += str(count) + c
            word = word[count:]

        return comp
