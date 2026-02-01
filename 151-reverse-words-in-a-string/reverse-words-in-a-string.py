class Solution:
    def reverseWords(self, s: str) -> str:
        q = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == " ":
                i += 1
                continue
            if i >= n:
                break
            j = i
            while j < n and s[j] != " ":
                j += 1
            word = s[i:j]
            q.append(word)
            i = j
        q.reverse()
        return " ".join(q)
