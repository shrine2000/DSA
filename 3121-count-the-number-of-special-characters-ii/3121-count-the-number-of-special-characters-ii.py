class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        li = [-1] * 26
        ui = [-1] * 26

        for i, char in enumerate(word):
            if char.islower():
                idx = ord(char) - ord("a")
                if ui[idx] != -1:
                    li[idx] = -10
                else:
                    li[idx] = i
            else:
                idx = ord(char) - ord("A")
                ui[idx] = i

        res = 0
        for i in range(26):
            if li[i] != -1 and li[i] != -10 and ui[i] != -1 and ui[i] > li[i]:
                res += 1

        return res
