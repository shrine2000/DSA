class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        max_freq = 0
        ans = 0
        
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            
            max_freq = max(max_freq, freq[idx])
            while (r - l + 1) - max_freq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)    
        return ans
            