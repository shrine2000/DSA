class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l, r = 0, n - 1

        while l < r and l < n - 1:
            temp2 =s[l]
            s[l] = s[r]
            s[r] = temp2
            l += 1
            r -= 1
        return s