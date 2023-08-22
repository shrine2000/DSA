class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        prefix_freq = [Counter()]
        
        for i in range(1, n + 1):
            prefix_freq.append(prefix_freq[i - 1] + Counter(s[i - 1]))
        
        total_beauty = 0
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring_freq = prefix_freq[j] - prefix_freq[i]
                max_freq = max(substring_freq.values(), default=0)
                min_freq = min(substring_freq.values(), default=0)
                total_beauty += max_freq - min_freq
        
        return total_beauty
