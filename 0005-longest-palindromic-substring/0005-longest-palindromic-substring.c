int isPalindrome(char* s, int start, int end) {
    while (start < end) {
        if (s[start] != s[end]) {
            return 0;
        }
        start++;
        end--;
    }
    return 1;
}

char* longestPalindrome(char* s) {
    int maxLength = 0;
    int start = 0;
    int end = 0;
    int len = strlen(s);
    
    for (int i = 0; i < len; i++) {
        for (int j = i; j < len; j++) {
            if (isPalindrome(s, i, j)) {
                int currLength = j - i + 1;
                if (currLength > maxLength) {
                    maxLength = currLength;
                    start = i;
                    end = j;
                }
            }
        }
    }
    
    char* result = (char*)malloc((maxLength + 1) * sizeof(char));
    strncpy(result, s + start, maxLength);
    result[maxLength] = '\0';
    
    return result;
}