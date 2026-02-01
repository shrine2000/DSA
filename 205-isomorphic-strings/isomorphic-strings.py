class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = [0] * 256
        m2 = [0] * 256

        for idx, (c1, c2) in enumerate(zip(s, t)):
            if m1[ord(c1)] != m2[ord(c2)]:
                return False

            m1[ord(c1)] = idx + 1
            m2[ord(c2)] = idx + 1

        return True
