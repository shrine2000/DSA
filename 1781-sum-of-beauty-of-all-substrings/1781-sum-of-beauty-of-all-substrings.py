class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        normalized_string = [ord(c) - ord('a') for c in s]
        
        for i in range(n - 1):
            char_count = [0] * 26  # 
            char_count[normalized_string[i]] = 1
            occurrences = [0] * n   
            occurrences[1] = 1
            max_occurrence = min_occurrence = 1
            
            for char in normalized_string[i + 1:]:
                occurrences[char_count[char]] -= 1
                char_count[char] += 1
                occurrences[char_count[char]] += 1
                
                if char_count[char] > max_occurrence:
                    max_occurrence = char_count[char]
                    
                if char_count[char] == 1:
                    min_occurrence = 1
                elif occurrences[min_occurrence] == 0:
                    min_occurrence += 1
                
                total_beauty += max_occurrence - min_occurrence
        
        return total_beauty
