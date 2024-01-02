class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        out = []

        for w in words:
            temp = w.split(separator)
            for t in temp:
                if t:
                    out.append(t)

        return out
