class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def helper(idx):
            if idx == len(s):
                return 1
            
            if s[idx] == '0':
                return 0
            
            single_digit = helper(idx + 1)
            two_digit = 0
            if (idx + 1 < len(s) and (s[idx] == '1' or (s[idx] == '2' and s[idx + 1] <= '6'))):
                two_digit = helper(idx + 2)
                
            return single_digit + two_digit
        return helper(0)