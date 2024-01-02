class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for c in s:
            if c == "i":
                r = res[::-1]
                res = r
            else:
                res += c
        return res
