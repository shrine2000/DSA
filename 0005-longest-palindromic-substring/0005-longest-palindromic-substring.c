class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            return string == string[::-1]
        
        longest = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if isPalindrome(substr) and len(substr) > len(longest):
                    longest = substr
        
        return longest
