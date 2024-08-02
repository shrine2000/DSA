class Solution:
    def reverseWords(self, s: str) -> str:
        final_str = ""
        temp = ""
        for i in range(len(s)):
            if s[i] != " ":
                temp += s[i]
            else:
                final_str += temp[::-1]
                final_str += " "
                temp =""
                
        if temp:
            final_str += temp[::-1]
            
        return final_str
                